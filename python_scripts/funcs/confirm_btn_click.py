from PyQt5.QtWidgets import QMessageBox
from python_scripts.utils import input_check
from python_scripts.data import filter_data


def btn_click(self):
    f_id = filter_data.filter_id
    f_name = filter_data.filter_name
    f_pics = filter_data.pics_path
    f_blends_str = filter_data.blend_mods
    all_digit = True
    for index, f_blend_str in enumerate(f_blends_str):
        for each_blend_str in f_blend_str:
            if not each_blend_str.isdigit():
                all_digit = False

    if not all_digit:
        QMessageBox.warning(self, '',
                            'blend格式错误',
                            QMessageBox.Yes)
        return

    for index, f_blend_str in enumerate(f_blends_str):
        filter_data.blend_modes_num[index] = []
        for each_blend_str in f_blend_str:
            filter_data.blend_modes_num[index].append((int(each_blend_str)))

    check_res = input_check.check(f_id, f_name, f_pics, filter_data.blend_modes_num)
    if check_res == -1:
        QMessageBox.warning(self, '',
                            '数据类型错误',
                            QMessageBox.Yes)
        return
    elif check_res == -2:
        QMessageBox.warning(self, '',
                            '滤镜id、滤镜name不能为空',
                            QMessageBox.Yes)
        return
    elif check_res == -3:
        QMessageBox.warning(self, '',
                            '滤镜id不符合格式要求,\n'
                            '只能包含字母、数字、下划线,\n'
                            '且不能以数字开头',
                            QMessageBox.Yes)
        return
    elif check_res == -4:
        QMessageBox.warning(self, '',
                            '请选择图片并添加滤镜',
                            QMessageBox.Yes)
        return
    elif check_res == -5:
        QMessageBox.warning(self, '',
                            '不支持该格式文件,\n'
                            '目前支持jpg、jpeg、png',
                            QMessageBox.Yes)
    elif check_res == -6:
        QMessageBox.warning(self, '',
                            '不支持的滤镜,\n'
                            '目前支持1,18,21',
                            QMessageBox.Yes)
    elif check_res != 1:
        QMessageBox.warning(self, '',
                            '发生预期以外错误',
                            QMessageBox.Yes)
    else:
        print('校验通过')
