# -*- coding: utf-8 -*-
"""
作者：3rd
时间：2022-08-20
功能：SHA512摘要计算
"""

import hashlib
import os
import sys

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
                               QMainWindow, QProgressBar, QSizePolicy, QSpacerItem,
                               QTextBrowser, QToolButton, QVBoxLayout, QWidget, QFileDialog)
import logo


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
        icon.addFile(u":/logo.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.selected_file_display.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
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
        self.algorithm_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"SHA-256", None))
        self.algorithm_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"SHA-512", None))

        self.algorithm_combo_box.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6458\u8981\u7b97\u6cd5", None))
        self.selected_file_display.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        # if QT_CONFIG(shortcut)
        self.quit.setShortcut(QCoreApplication.translate("MainWindow", u"Esc", None))
        # endif // QT_CONFIG(shortcut)
        self.clear_screen_button.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
        # if QT_CONFIG(shortcut)
        self.clear_screen_button.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
        # endif // QT_CONFIG(shortcut)
        self.calculate_button.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        # if QT_CONFIG(shortcut)
        self.calculate_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        # endif // QT_CONFIG(shortcut)
        # retranslateUi

    def select_file(self):
        """文件选择按钮回调。"""
        # noinspection PyTypeChecker
        filename, filetype = QFileDialog.getOpenFileName(None,
                                                         "选取文件",
                                                         "",
                                                         "All Files (*);;Text Files (*.txt)")
        self.selected_file_display.setText(filename)

    def calculate_hash(self):
        """计算按钮回调，进行摘要计算。"""
        file_name = self.selected_file_display.text()
        if file_name == "":
            return self.result_output.insertPlainText("请选择文件！\n")

        selected_algorithm = self.algorithm_combo_box.currentText()
        if selected_algorithm == "SHA-512":
            algorithm = hashlib.sha512()
        elif selected_algorithm == "SHA-256":
            algorithm = hashlib.sha256()
        else:
            algorithm = hashlib.md5()

        with open(file_name, "rb") as file:
            file_size = os.path.getsize(file_name)
            current_progress = 0
            while True:
                file_chunk = file.read(65536)
                current_progress += len(file_chunk)
                self.progress_bar.setValue(current_progress / file_size * 100)
                if not file_chunk:
                    break
                algorithm.update(file_chunk)

        self.result_output.insertPlainText(
            file_name
            + "的摘要为（已存至剪贴板）：\n"
            + algorithm.hexdigest()
            + '\n\n')
        clipboard = QApplication.clipboard()  # 创建剪切板对象
        clipboard.setText(algorithm.hexdigest())  # 用于向剪切板写入文本

    def quit_program(self):
        """退出按钮回调。"""
        QCoreApplication.quit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
