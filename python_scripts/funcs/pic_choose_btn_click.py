from PyQt5 import QtWidgets
import os


def btn_click(self, index):
    print(index)
    file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                 "All Files(*);;Text Files(*.txt)")
    # print(file_name)
    # print(file_type)
