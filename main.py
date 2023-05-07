# -*- coding: utf-8 -*-
"""
作者：3rd
时间：2022-08-20
功能：文件哈希摘要计算
"""

import logo
from Ui_MainWindow import *

from PySide6.QtWidgets import QFileDialog

import hashlib
import os
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/logo.png"))
        # 开启拖拽功能
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls() and event.mimeData().urls()[0].isLocalFile():
            # 只接受拖拽进来的第一个文件，并且该文件是本地文件
            event.accept()
            return
        event.ignore()

    def dropEvent(self, event):
        path = event.mimeData().urls()[0].toLocalFile()
        if os.path.isdir(path):
            return
        else:  # 处理拖拽进来的文件
            self.selected_file_display.setText(path)
            self.calculate_hash()

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
            self.result_output.insertPlainText("请选择文件！\n")
            return

        selected_algorithm = self.algorithm_combo_box.currentText().lower()
        if hasattr(hashlib, selected_algorithm):
            algorithm = getattr(hashlib, selected_algorithm)()
        else:
            algorithm = hashlib.md5()

        with open(file_name, "rb") as file:
            file_size = os.path.getsize(file_name)
            current_progress = 0

            while current_progress < file_size:
                file_chunk = file.read(65536)
                algorithm.update(file_chunk)
                current_progress += len(file_chunk)
                self.progress_bar.setValue((current_progress / file_size) * 100)
            self.progress_bar.setValue(100)

        # 光标移到文本结尾。
        # cursor = self.result_output.textCursor()
        # self.result_output.moveCursor(cursor.End)

        self.result_output.append(
            file_name
            + "的摘要为（已存至剪贴板）：\n"
            + algorithm.hexdigest())
        self.result_output.insertHtml("<hr><p></p>")  # 添加分割线，可能会导致排版混乱

        # 进度条自动滚至底部。
        v_scroll_bar = self.result_output.verticalScrollBar()
        v_scroll_bar.setValue(v_scroll_bar.maximum())

        # 创建剪切板对象，复制文本。
        clipboard = QApplication.clipboard()
        clipboard.setText(algorithm.hexdigest())

    def quit_program(self):
        """退出按钮回调。"""
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
