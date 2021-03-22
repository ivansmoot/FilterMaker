from PyQt5 import QtWidgets
from pathlib import Path
from python_scripts.data import filter_data


def btn_click(self, index):
    file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "选择图片",
        str(Path.cwd()),
        "Pics(*.png *.jpg *.jpeg *.acv)"
    )
    filter_data.pics_path[index] = file_name
