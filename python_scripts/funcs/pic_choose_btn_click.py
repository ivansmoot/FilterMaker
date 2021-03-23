from PyQt5 import QtWidgets
from pathlib import Path
from python_scripts.data import filter_data


def btn_click(self, index, btn):
    file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "选择图片",
        str(Path(filter_data.current_path)),
        "Pics(*.png *.jpg *.jpeg *.acv)"
    )
    filter_data.pics_path[index] = file_name
    # cancel不需要修改按钮名称
    if str(file_name) is not '':
        filter_data.pic_choose_btn_name[index] = str(file_name).split('/')[-1]
    btn.setText(filter_data.pic_choose_btn_name[index])
