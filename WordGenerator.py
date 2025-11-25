# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WordGenerator.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.Canada))
        self.actionFileExport = QAction(MainWindow)
        self.actionFileExport.setObjectName(u"actionFileExport")
        self.actionHelpApplication_Guide = QAction(MainWindow)
        self.actionHelpApplication_Guide.setObjectName(u"actionHelpApplication_Guide")
        self.actionFileSave = QAction(MainWindow)
        self.actionFileSave.setObjectName(u"actionFileSave")
        self.actionFileLoad = QAction(MainWindow)
        self.actionFileLoad.setObjectName(u"actionFileLoad")
        self.actionHelpGithub_Repository = QAction(MainWindow)
        self.actionHelpGithub_Repository.setObjectName(u"actionHelpGithub_Repository")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelVowels = QLabel(self.centralwidget)
        self.labelVowels.setObjectName(u"labelVowels")

        self.verticalLayout.addWidget(self.labelVowels)

        self.textVowels = QPlainTextEdit(self.centralwidget)
        self.textVowels.setObjectName(u"textVowels")
        self.textVowels.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.textVowels)

        self.labelConsonants = QLabel(self.centralwidget)
        self.labelConsonants.setObjectName(u"labelConsonants")

        self.verticalLayout.addWidget(self.labelConsonants)

        self.textConsonants = QPlainTextEdit(self.centralwidget)
        self.textConsonants.setObjectName(u"textConsonants")
        self.textConsonants.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.textConsonants)

        self.labelBanned_Clusters = QLabel(self.centralwidget)
        self.labelBanned_Clusters.setObjectName(u"labelBanned_Clusters")

        self.verticalLayout.addWidget(self.labelBanned_Clusters)

        self.textBanned_Clusters = QPlainTextEdit(self.centralwidget)
        self.textBanned_Clusters.setObjectName(u"textBanned_Clusters")
        self.textBanned_Clusters.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.textBanned_Clusters)

        self.labelRomanization_Mapping = QLabel(self.centralwidget)
        self.labelRomanization_Mapping.setObjectName(u"labelRomanization_Mapping")

        self.verticalLayout.addWidget(self.labelRomanization_Mapping)

        self.textRomanization_Mapping = QPlainTextEdit(self.centralwidget)
        self.textRomanization_Mapping.setObjectName(u"textRomanization_Mapping")
        self.textRomanization_Mapping.setTabChangesFocus(True)

        self.verticalLayout.addWidget(self.textRomanization_Mapping)

        self.labelConstraints = QLabel(self.centralwidget)
        self.labelConstraints.setObjectName(u"labelConstraints")

        self.verticalLayout.addWidget(self.labelConstraints)

        self.textConstraints = QLineEdit(self.centralwidget)
        self.textConstraints.setObjectName(u"textConstraints")

        self.verticalLayout.addWidget(self.textConstraints)

        self.labelConstraint_Probability = QLabel(self.centralwidget)
        self.labelConstraint_Probability.setObjectName(u"labelConstraint_Probability")

        self.verticalLayout.addWidget(self.labelConstraint_Probability)

        self.spinConstraint_Probability = QDoubleSpinBox(self.centralwidget)
        self.spinConstraint_Probability.setObjectName(u"spinConstraint_Probability")
        self.spinConstraint_Probability.setMaximum(1.000000000000000)
        self.spinConstraint_Probability.setSingleStep(0.050000000000000)

        self.verticalLayout.addWidget(self.spinConstraint_Probability)

        self.labelSyllable_Maximum = QLabel(self.centralwidget)
        self.labelSyllable_Maximum.setObjectName(u"labelSyllable_Maximum")

        self.verticalLayout.addWidget(self.labelSyllable_Maximum)

        self.spinSyllable_Maximum = QSpinBox(self.centralwidget)
        self.spinSyllable_Maximum.setObjectName(u"spinSyllable_Maximum")

        self.verticalLayout.addWidget(self.spinSyllable_Maximum)

        self.labelSyllable_Probability = QLabel(self.centralwidget)
        self.labelSyllable_Probability.setObjectName(u"labelSyllable_Probability")

        self.verticalLayout.addWidget(self.labelSyllable_Probability)

        self.spinSyllable_Probability = QDoubleSpinBox(self.centralwidget)
        self.spinSyllable_Probability.setObjectName(u"spinSyllable_Probability")
        self.spinSyllable_Probability.setMaximum(1.000000000000000)
        self.spinSyllable_Probability.setSingleStep(0.050000000000000)

        self.verticalLayout.addWidget(self.spinSyllable_Probability)

        self.labelMinimum_Letters = QLabel(self.centralwidget)
        self.labelMinimum_Letters.setObjectName(u"labelMinimum_Letters")

        self.verticalLayout.addWidget(self.labelMinimum_Letters)

        self.spinMinimum_Phonemes = QSpinBox(self.centralwidget)
        self.spinMinimum_Phonemes.setObjectName(u"spinMinimum_Phonemes")

        self.verticalLayout.addWidget(self.spinMinimum_Phonemes)

        self.labelCredit = QLabel(self.centralwidget)
        self.labelCredit.setObjectName(u"labelCredit")

        self.verticalLayout.addWidget(self.labelCredit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.labelWords = QLabel(self.centralwidget)
        self.labelWords.setObjectName(u"labelWords")

        self.verticalLayout_6.addWidget(self.labelWords)

        self.spinNumberWords = QSpinBox(self.centralwidget)
        self.spinNumberWords.setObjectName(u"spinNumberWords")
        self.spinNumberWords.setMaximum(65536)
        self.spinNumberWords.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.verticalLayout_6.addWidget(self.spinNumberWords)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkRepeated_Vowels = QCheckBox(self.centralwidget)
        self.checkRepeated_Vowels.setObjectName(u"checkRepeated_Vowels")

        self.horizontalLayout.addWidget(self.checkRepeated_Vowels)

        self.checkRepeated_Consonants = QCheckBox(self.centralwidget)
        self.checkRepeated_Consonants.setObjectName(u"checkRepeated_Consonants")

        self.horizontalLayout.addWidget(self.checkRepeated_Consonants)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.buttonGenerate = QPushButton(self.centralwidget)
        self.buttonGenerate.setObjectName(u"buttonGenerate")

        self.verticalLayout_6.addWidget(self.buttonGenerate)

        self.textGeneratedWords = QPlainTextEdit(self.centralwidget)
        self.textGeneratedWords.setObjectName(u"textGeneratedWords")
        self.textGeneratedWords.setTabChangesFocus(True)

        self.verticalLayout_6.addWidget(self.textGeneratedWords)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.appStatusBar = QStatusBar(MainWindow)
        self.appStatusBar.setObjectName(u"appStatusBar")
        MainWindow.setStatusBar(self.appStatusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionFileSave)
        self.menuFile.addAction(self.actionFileLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionFileExport)
        self.menuHelp.addAction(self.actionHelpApplication_Guide)
        self.menuHelp.addAction(self.actionHelpGithub_Repository)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple Word Generator", None))
        self.actionFileExport.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
#if QT_CONFIG(shortcut)
        self.actionFileExport.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelpApplication_Guide.setText(QCoreApplication.translate("MainWindow", u"Application Guide", None))
#if QT_CONFIG(shortcut)
        self.actionHelpApplication_Guide.setShortcut(QCoreApplication.translate("MainWindow", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.actionFileSave.setText(QCoreApplication.translate("MainWindow", u"Save Config...", None))
#if QT_CONFIG(shortcut)
        self.actionFileSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionFileLoad.setText(QCoreApplication.translate("MainWindow", u"Load Config...", None))
#if QT_CONFIG(shortcut)
        self.actionFileLoad.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionHelpGithub_Repository.setText(QCoreApplication.translate("MainWindow", u"Github Repository", None))
        self.labelVowels.setText(QCoreApplication.translate("MainWindow", u"Vowels", None))
        self.labelConsonants.setText(QCoreApplication.translate("MainWindow", u"Consonants", None))
        self.labelBanned_Clusters.setText(QCoreApplication.translate("MainWindow", u"Banned Clusters", None))
        self.labelRomanization_Mapping.setText(QCoreApplication.translate("MainWindow", u"Romanization Mapping", None))
        self.labelConstraints.setText(QCoreApplication.translate("MainWindow", u"Constraints", None))
        self.labelConstraint_Probability.setText(QCoreApplication.translate("MainWindow", u"Constraint Probability", None))
        self.labelSyllable_Maximum.setText(QCoreApplication.translate("MainWindow", u"Syllable Maximum", None))
        self.spinSyllable_Maximum.setSuffix(QCoreApplication.translate("MainWindow", u" Syllables", None))
        self.labelSyllable_Probability.setText(QCoreApplication.translate("MainWindow", u"Syllable Probability", None))
        self.labelMinimum_Letters.setText(QCoreApplication.translate("MainWindow", u"Minimum Number of Phonemes", None))
        self.spinMinimum_Phonemes.setSuffix(QCoreApplication.translate("MainWindow", u" Phonemes", None))
        self.labelCredit.setText(QCoreApplication.translate("MainWindow", u"Made by ika4422 |\u00a0With Contributions from umi4422 & are4422", None))
        self.labelWords.setText(QCoreApplication.translate("MainWindow", u"Number of Words", None))
        self.spinNumberWords.setSuffix(QCoreApplication.translate("MainWindow", u" Words", None))
        self.checkRepeated_Vowels.setText(QCoreApplication.translate("MainWindow", u"Ban Repeated Vowels", None))
        self.checkRepeated_Consonants.setText(QCoreApplication.translate("MainWindow", u"Ban Repeated Consonants", None))
        self.buttonGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate Words", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

