#!/usr/bin/env python3

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
def strip_chars(string):
    for i in ['\n', ' ']:
        string = string.replace(i, '')

    return string

def multi_replace(s, replacements):
    substrs = sorted([str(key) for key in replacements.keys()], key=len, reverse=True)
    pattern = re.compile("|".join(map(re.escape, substrs)))
    
    return pattern.sub(lambda m: replacements[m.group(0)], s)

# function to generate singular word
def word_generation(
        vowels,
        consonants,
        constraints,
        syllabic_probability,
        syllabic_limit,
        constraint_probability
    ):
    word = []

    i = 0
    while i < syllabic_limit:
        syllable = []

        # generate each phoneme at a time
        for phoneme in constraints:
            generate = True

            # find if phoneme contains specific probability
            try:
                specific_probability = round(float(re.findall(r"[-+]?(?:\d*\.*\d+)", phoneme)[0]), 2)
                if 0.0 < specific_probability and specific_probability < 1.0:
                    constraint_probability = specific_probability
            except:
                pass

            # if phoneme is optional randomly determine if it is generated or not
            if '*' in phoneme:
                generate = random.random() <= constraint_probability

            # if random choice determines generation to not generate the phoneme skip to next phoneme
            if not generate:
                continue

            # append randomly selected phoneme according to related class symbol, currently only supports predefined class symbols
            if 'V' in phoneme:
                syllable.append(random.choice(vowels))

            if 'C' in phoneme:
                syllable.append(random.choice(consonants))
        
        # if a syllable was determines append it to the word list
        if syllable:
            word.append(syllable)
            i += 1

        # determine according to random probability if the next syllable is generated
        if random.random() >= syllabic_probability:
            break
    
    return word

# function to generate a list of words
def word_list_generation(
        vowels,
        consonants,
        constraints,
        syllabic_probability,
        syllabic_limit,
        banned_clusters,
        minimum_phonemes,
        num_words,
        constraint_probability
    ) -> list[str]:
    # initialize variables
    banned_clusters = [s for s in banned_clusters if s != '']

    word_list = []
    cycles = 0

    # generate words until the word list contains the wanted number of words
    while len(word_list) < num_words:
        # if the generation times out then display an error message instead of having an infinite loop
        if cycles >= (num_words ** 2 + 1024):
            QtWidgets.QMessageBox.critical(None, 'Error!', 'Word generation loop timed out! Consider checking that your settings can define any words.')
            break

        # call word generation method
        word = word_generation(
            vowels,
            consonants,
            constraints,
            syllabic_probability,
            syllabic_limit,
            constraint_probability
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
        if not any(cluster in word_str for cluster in banned_clusters) and not num_phonemes < minimum_phonemes and not word_str in word_list:
            word_list.append(word_str)

        cycles += 1

    return word_list

# window class
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # menu bar options
        self.actionFileExport.triggered.connect(self.action_export)
        self.actionFileSave.triggered.connect(self.action_save_config)
        self.actionFileLoad.triggered.connect(self.action_load_config)
        self.actionHelpApplication_Guide.triggered.connect(self.action_open_guide)
        self.actionHelpGithub_Repository.triggered.connect(self.action_open_repo)

        # triggers
        self.buttonGenerate.clicked.connect(self.generate_words)

    def action_export(self):
        # open file dialogue
        filename, file_filter = QtWidgets.QFileDialog.getSaveFileName(
            self,
            'Save Word List',
            '',
            'CSV Files (*.csv);;Text Files (*.txt)'
        )
        if not filename:
            return
        
        # determine if file type is .csv or .txt
        is_csv = False
        if (file_filter and 'csv' in file_filter.lower()) or (filename.lower().endswith('.csv')):
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

    def action_save_config(self):
        # fetch data from fields and insert into dictionary
        save_data = {}
        try:
            save_data = {
                'vowels': self.textVowels.toPlainText(),
                'consonants': self.textConsonants.toPlainText(),
                'bannedClusters': self.textBanned_Clusters.toPlainText(),
                'romanizationMapping': self.textRomanization_Mapping.toPlainText(),
                'constraints': self.textConstraints.text(),
                'constraintsProbability': round(self.spinConstraint_Probability.value(), 2),
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
                json.dump(save_data, f, ensure_ascii=False, indent=2)
            try:
                # successful write to file
                self.appStatusBar.showMessage(f'Configuration saved to {pathlib.Path(filename).name}', 5000)
            except Exception:
                pass
        # display error popup if save fails
        except Exception:
            self.appStatusBar.showMessage('Failed to save configuration', 5000)

    def action_load_config(self):
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
        except Exception:
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
            if 'constraintsProbability' in data:
                self.spinConstraint_Probability.setValue(round(float(data['constraintsProbability']), 2))
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

    @staticmethod
    def action_open_guide():
        # open to usage section of README on GitHub repo
        webbrowser.open("https://github.com/ika4422/simple-word-generator/tree/main?tab=readme-ov-file#usage")

    @staticmethod
    def action_open_repo():
        # open to GitHub repo for project
        webbrowser.open("https://github.com/ika4422/simple-word-generator")

    def generate_words(self):
        # clear the output field
        self.textGeneratedWords.clear()

        # fetch data from input fields and serialize data
        consonants = strip_chars(self.textConsonants.toPlainText()).split(',')
        vowels = strip_chars(self.textVowels.toPlainText()).split(',')

        constraints = strip_chars(self.textConstraints.text().upper()).split(',')
        constraints_probability = self.spinConstraint_Probability.value()

        syllable_probability = self.spinSyllable_Probability.value()
        syllable_maximum = self.spinSyllable_Maximum.value()
        
        banned_clusters = strip_chars(self.textBanned_Clusters.toPlainText()).split(',')
        banned_clusters = [s for s in banned_clusters if s != '']

        minimum_phonemes = self.spinMinimum_Phonemes.value()
        number_words = self.spinNumberWords.value()

        # add to banned_clusters list repeated vowels or consonants if relevant checkbox is checked
        if self.checkRepeated_Consonants.isChecked():
            for phoneme in consonants:
                banned_clusters.append(phoneme * 2)

        if self.checkRepeated_Vowels.isChecked():
            for phoneme in vowels:
                banned_clusters.append(phoneme * 2)

        # call word generation method from methods file
        words = word_list_generation(
                vowels,
                consonants,
                constraints,
                syllable_probability,
                syllable_maximum,
                banned_clusters,
                minimum_phonemes,
                number_words,
                constraints_probability
        )

        # only execute this section if there are romanization mappings
        if self.textRomanization_Mapping.toPlainText() != '':
            # initialize variables
            ipa_words = words
            words = []
            romanization_map = {}

            # parse romanization map into dict
            for mapping in strip_chars(self.textRomanization_Mapping.toPlainText()).split(','):
                split_mapping = mapping.split(':')
                ipa_char = split_mapping[0].strip()
                roman_char = split_mapping[1].strip()
                romanization_map[ipa_char] = roman_char
            
            # apply romanization rules to ipa words
            for ipa_word in ipa_words:
                roman_word = multi_replace(ipa_word, romanization_map)
                words.append(f'{roman_word} : {ipa_word}')

        # sort alphabetically and convert to string for display
        words.sort()
        words_str = '\n'.join(words)
        self.textGeneratedWords.insertPlainText(words_str)
        self.appStatusBar.showMessage(f'Generated {number_words} words successfully!', 5000)

# application entry point
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
