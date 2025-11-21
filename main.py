# standard imports
import sys
import webbrowser
import pathlib
import json
import csv
import random
import re

# library imports
from PySide6 import QtWidgets

# local imports
from WordGenerator import Ui_MainWindow

# function to remove new lines and spaces from a string
def stripChars(string):
    for i in ['\n', ' ']:
        string = string.replace(i, '')

    return string

def multiReplace(s, replacements):
    substrs = sorted(replacements.keys(), key=len, reverse=True)
    pattern = re.compile("|".join(map(re.escape, substrs)))
    
    return pattern.sub(lambda m: replacements[m.group(0)], s)

# function to generate singular word
def wordGeneration(
        vowels,
        consonants,
        constraints,
        syllabicProbability,
        syllabicLimit
    ):
    word = []

    i = 0
    while i < syllabicLimit:
        syllable = []

        # generate each phoneme at a time
        for element in constraints:
            generate = True

            # if phoneme is optional randomly determine if it is generated or not
            if '*' in element:
                generate = random.choice([True, False])

            # if random choice determines generation to not generate the phoneme skip to next phoneme
            if not generate:
                continue

            # append randomly selected phoneme according to related class symbol, currently only supports predefined class symbols
            if 'V' in element:
                syllable.append(random.choice(vowels))

            if 'C' in element:
                syllable.append(random.choice(consonants))
        
        # if a syllable was determines append it to the word list
        if syllable:
            word.append(syllable)
            i += 1

        # determine according to random probability if the next syllable is generated
        if random.random() >= syllabicProbability:
            break
    
    return word

# function to generate a list of words
def wordListGeneration(
        vowels,
        consonants,
        constraints,
        syllabicProbability,
        syllabicLimit,
        bannedClusters,
        minimumPhonemes,
        numWords
    ) -> list[str]:
    # initialize variables
    bannedClusters = [s for s in bannedClusters if s != '']

    wordList = []
    cycles = 0

    # generate words until the word list contains the wanted number of words
    while len(wordList) < numWords:
        # if the generation times out then display an error message instead of having an infinite loop
        if cycles >= (numWords**2 + 1024):
            QtWidgets.QMessageBox.critical(None, 'Error!', 'Word generation loop timed out! Consider checking that your settings can define any words.')
            break

        # call word generation method
        word = wordGeneration(
            vowels,
            consonants,
            constraints,
            syllabicProbability,
            syllabicLimit
        )

        # count number of phonemes in the word
        num_phonemes = 0
        for i in word:
            for _ in i:
                num_phonemes += 1

        # create word string
        syllables = []
        for i in word:
            syllables.append(''.join(i))
        word_str = ''.join(syllables)

        # ensure that the generated word follows the defined rules before appending to word list
        if not any(cluster in word_str for cluster in bannedClusters) and not num_phonemes < minimumPhonemes and not word_str in wordList:
            wordList.append(word_str)

        cycles += 1

    return wordList

# window class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # menu bar options
        self.actionFileExport.triggered.connect(self.actionExport)
        self.actionFileSave.triggered.connect(self.actionSaveConfig)
        self.actionFileLoad.triggered.connect(self.actionLoadConfig)
        self.actionHelpApplication_Guide.triggered.connect(self.actionOpenGuide)
        self.actionHelpGithub_Repository.triggered.connect(self.actionOpenRepo)

        # triggers
        self.buttonGenerate.clicked.connect(self.generateWords)

    def actionExport(self):
        # open file dialogue
        filename, filter = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Save Word List',
            '',
            'CSV Files (*.csv);;Text Files (*.txt)'
        )
        if not filename:
            return
        
        # determine if file type is .csv or .txt
        is_csv = False
        if (filter and 'csv' in filter.lower()) or (filename.lower().endswith('.csv')):
            is_csv = True

        # ensure file has file type in name
        if is_csv and not filename.lower().endswith('.csv'):
            filename += '.csv'
        if not is_csv and not filename.lower().endswith('.txt'):
            filename += '.txt'

        try:
            # fetch word list and split into lines
            text = self.textGeneratedWords.toPlainText()
            lines = [l for l in text.splitlines() if l.strip() != '']

            # csv export code
            if is_csv:
                with open(filename, 'w', encoding='utf-8', newline='') as f:
                    # create writer and add top row
                    writer = csv.writer(f)
                    writer.writerow(['Romanization', 'IPA'])

                    # split line into roman and ipa words
                    roman, ipa = '', ''
                    for line in lines:
                        if ' : ' in line:
                            roman, ipa = line.split(' : ', 1)
                        elif '\t' in line:
                            roman, ipa = line.split('\t', 1)
                        elif ',' in line and line.count(',') == 1:
                            roman, ipa = line.split(',', 1)
                        else:
                            roman, ipa = line, ''
                    
                        # write roman and ipa to columns
                        writer.writerow([roman.strip(), ipa.strip()])
            # text file export code
            else:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
            
            # successful export of data
            self.appStatusBar.showMessage(f'Saved word list to {pathlib.Path(filename).name}!')
        # display error in box if failed
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, 'Error!', f'Failed to save {pathlib.Path(filename).name}: {e}')
            self.appStatusBar.showMessage(f'Failed to save {pathlib.Path(filename).name}!', 5000)

    def actionSaveConfig(self):
        # fetch data from fields and insert into dictionary
        saveData = {}
        try:
            saveData = {
                'vowels': self.textVowels.toPlainText(),
                'consonants': self.textConsonants.toPlainText(),
                'bannedClusters': self.textBanned_Clusters.toPlainText(),
                'romanizationMapping': self.textRomanization_Mapping.toPlainText(),
                'constraints': self.textConstraints.text(),
                'syllableMaximum': self.spinSyllable_Maximum.value(),
                'syllableProbability': round(self.spinSyllable_Probability.value(), 2),
                'minimumPhonemes': self.spinMinimum_Phonemes.value(),
                'numberWords': self.spinNumberWords.value(),
                'banRepeatVowels': self.checkRepeated_Vowels.isChecked(),
                'banRepeatConsonants': self.checkRepeated_Consonants.isChecked()
            }
        except Exception:
            pass

        # open file save dialogue
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Save Configuration',
            '',
            'JSON Files (*.json);;All Files (*)'
        )
        if not filename:
            return

        # ensure file name contains file extension
        if not filename.lower().endswith('.json'):
            filename += '.json'

        try:
            # save to json file containing dictionary
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(saveData, f, ensure_ascii=False, indent=2)
            try:
                # successful write to file
                self.appStatusBar.showMessage(f'Configuration saved to {pathlib.Path(filename).name}', 5000)
            except Exception:
                pass
        # display error popup if save fails
        except Exception as e:
            self.appStatusBar.showMessage('Failed to save configuration', 5000)

    def actionLoadConfig(self):
        # open file open dialogue and exit method if none selected
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Load Configuration',
            '',
            'JSON Files (*.json);;All Files (*)'
        )
        if not filename:
            return

        # load data from selected file into data dictionary
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        # display error popup if load fails
        except Exception as e:
            self.appStatusBar.showMessage('Failed to load configuration', 5000)
            return

        # attempt to retrieve and insert data into fields
        try:
            self.textVowels.setPlainText(data.get('vowels', ''))
            self.textConsonants.setPlainText(data.get('consonants', ''))
            self.textBanned_Clusters.setPlainText(data.get('bannedClusters', ''))
            self.textRomanization_Mapping.setPlainText(data.get('romanizationMapping', ''))
            self.textConstraints.setText(data.get('constraints', ''))
        except Exception:
            pass

        try:
            if 'syllableMaximum' in data:
                self.spinSyllable_Maximum.setValue(int(data['syllableMaximum']))
            if 'syllableProbability' in data:
                self.spinSyllable_Probability.setValue(round(float(data['syllableProbability']), 2))
            if 'minimumPhonemes' in data:
                self.spinMinimum_Phonemes.setValue(int(data['minimumPhonemes']))
            if 'numberWords' in data:
                self.spinNumberWords.setValue(int(data['numberWords']))
        except Exception:
            pass

        try:
            self.checkRepeated_Vowels.setChecked(bool(data.get('banRepeatVowels', False)))
            self.checkRepeated_Consonants.setChecked(bool(data.get('banRepeatConsonants', False)))
        except Exception:
            pass

        try:
            self.appStatusBar.showMessage(f'Loaded configuration from {pathlib.Path(filename).name}', 5000)
        except Exception:
            pass

    def actionOpenGuide(self):
        # open to usage section of README on github repo
        webbrowser.open("https://github.com/ika4422/simple-word-generator/tree/main?tab=readme-ov-file#usage")

    def actionOpenRepo(self):
        # open to github repo for project
        webbrowser.open("https://github.com/ika4422/simple-word-generator")

    def generateWords(self):
        # clear the output field
        self.textGeneratedWords.clear()

        # fetch data from input fields and serialize data
        consonants = stripChars(self.textConsonants.toPlainText()).split(',')
        vowels = stripChars(self.textVowels.toPlainText()).split(',')

        constraints = stripChars(self.textConstraints.text().upper()).split(',')

        syllableProbability = self.spinSyllable_Probability.value()
        syllableMaximum = self.spinSyllable_Maximum.value()
        
        bannedClusters = stripChars(self.textBanned_Clusters.toPlainText()).split(',')
        bannedClusters = [s for s in bannedClusters if s != '']

        minimumPhonemes = self.spinMinimum_Phonemes.value()
        numberWords = self.spinNumberWords.value()

        # add to bannedClusters list repeated vowels or consonants if relevant checkbox is checked
        if self.checkRepeated_Consonants.isChecked():
            for phoneme in consonants:
                bannedClusters.append(phoneme * 2)

        if self.checkRepeated_Vowels.isChecked():
            for phoneme in vowels:
                bannedClusters.append(phoneme * 2)

        # call word generation method from methods file
        words = wordListGeneration(
                vowels,
                consonants,
                constraints,
                syllableProbability,
                syllableMaximum,
                bannedClusters,
                minimumPhonemes,
                numberWords
        )

        # only execute this section if there are romanization mappings
        if self.textRomanization_Mapping.toPlainText() != '':
            # initialize variables
            ipa_words = words
            words = []
            romanizationMap = {}

            # parse romanization map into dict
            for set in stripChars(self.textRomanization_Mapping.toPlainText()).split(','):
                splitSet = set.split(':')
                ipa_char = splitSet[0].strip()
                roman_char = splitSet[1].strip()
                romanizationMap[ipa_char] = roman_char
            
            # apply romanization rules to ipa words
            for ipa_word in ipa_words:
                roman_word = multiReplace(ipa_word, romanizationMap)
                words.append(f'{roman_word} : {ipa_word}')

        # sort alphabetically and convert to string for display
        words.sort()
        words_str = '\n'.join(words)
        self.textGeneratedWords.insertPlainText(words_str)
        self.appStatusBar.showMessage(f'Generated {numberWords} words successfully!', 5000)

# application entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
