# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QProgressBar, QSizePolicy, QSpacerItem,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(300, 300))
        font = QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.main_layout = QGridLayout(self.main_widget)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName(u"vertical_layout")
        self.option_layout = QGridLayout()
        self.option_layout.setSpacing(0)
        self.option_layout.setObjectName(u"option_layout")
        self.select_file_button = QToolButton(self.main_widget)
        self.select_file_button.setObjectName(u"select_file_button")

        self.option_layout.addWidget(self.select_file_button, 0, 1, 1, 1)

        self.algorithm_combo_box = QComboBox(self.main_widget)
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.addItem("")
        self.algorithm_combo_box.setObjectName(u"algorithm_combo_box")

        self.option_layout.addWidget(self.algorithm_combo_box, 1, 0, 1, 2)

        self.selected_file_display = QLineEdit(self.main_widget)
        self.selected_file_display.setObjectName(u"selected_file_display")
        self.selected_file_display.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selected_file_display.sizePolicy().hasHeightForWidth())
        self.selected_file_display.setSizePolicy(sizePolicy)
        self.selected_file_display.setCursor(QCursor(Qt.IBeamCursor))
        self.selected_file_display.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.selected_file_display.setReadOnly(True)

        self.option_layout.addWidget(self.selected_file_display, 0, 0, 1, 1)


        self.vertical_layout.addLayout(self.option_layout)

        self.control_layout = QGridLayout()
        self.control_layout.setSpacing(0)
        self.control_layout.setObjectName(u"control_layout")
        self.quit = QToolButton(self.main_widget)
        self.quit.setObjectName(u"quit")

        self.control_layout.addWidget(self.quit, 0, 4, 1, 1)

        self.horizontal_spacer_0 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_layout.addItem(self.horizontal_spacer_0, 0, 1, 1, 1)

        self.clear_screen_button = QToolButton(self.main_widget)
        self.clear_screen_button.setObjectName(u"clear_screen_button")

        self.control_layout.addWidget(self.clear_screen_button, 0, 2, 1, 1)

        self.calculate_button = QToolButton(self.main_widget)
        self.calculate_button.setObjectName(u"calculate_button")

        self.control_layout.addWidget(self.calculate_button, 0, 0, 1, 1)

        self.horizontal_spacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_layout.addItem(self.horizontal_spacer_1, 0, 3, 1, 1)


        self.vertical_layout.addLayout(self.control_layout)

        self.log_layout = QGridLayout()
        self.log_layout.setSpacing(0)
        self.log_layout.setObjectName(u"log_layout")
        self.result_output = QTextBrowser(self.main_widget)
        self.result_output.setObjectName(u"result_output")
        self.result_output.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.result_output.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.log_layout.addWidget(self.result_output, 0, 0, 1, 1)

        self.progress_bar = QProgressBar(self.main_widget)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(0)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setOrientation(Qt.Horizontal)
        self.progress_bar.setInvertedAppearance(False)

        self.log_layout.addWidget(self.progress_bar, 1, 0, 1, 2)


        self.vertical_layout.addLayout(self.log_layout)


        self.main_layout.addLayout(self.vertical_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)

        self.retranslateUi(MainWindow)
        self.calculate_button.clicked.connect(MainWindow.calculate_hash)
        self.clear_screen_button.clicked.connect(self.result_output.clear)
        self.quit.clicked.connect(MainWindow.quit_program)
        self.select_file_button.clicked.connect(MainWindow.select_file)

        self.algorithm_combo_box.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6458\u8981\u8ba1\u7b97V0.0.1", None))
        self.select_file_button.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.algorithm_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"MD5", None))
        self.algorithm_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"SHA256", None))
        self.algorithm_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"SHA512", None))
        self.algorithm_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"SHA1", None))
        self.algorithm_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"SHA224", None))
        self.algorithm_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"SHA384", None))

        self.algorithm_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6458\u8981\u7b97\u6cd5", None))
        self.selected_file_display.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
#if QT_CONFIG(shortcut)
        self.quit.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.clear_screen_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
#if QT_CONFIG(shortcut)
        self.clear_screen_button.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
#if QT_CONFIG(shortcut)
        self.calculate_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

