from PyQt5 import QtWidgets
from pathlib import Path
from python_scripts.data import filter_data


def btn_click(self, index, btn):
    support_pic = 'Pics('
    for support_pic_format in filter_data.support_pic_formats:
        support_pic += '*.'
        support_pic += support_pic_format
        support_pic += ' '
    support_pic += ')'
    file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(
        self,
        "选择图片",
        str(Path(filter_data.current_path)),
        support_pic
    )
    filter_data.pics_path[index] = file_name
    # cancel不需要修改按钮名称
    if str(file_name) != '':
        filter_data.pic_choose_btn_name[index] = str(file_name).split('/')[-1]
    btn.setText(filter_data.pic_choose_btn_name[index])
