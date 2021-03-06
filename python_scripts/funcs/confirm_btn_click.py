from PyQt5.QtWidgets import QMessageBox
from python_scripts.utils import input_check
from python_scripts.data import filter_data
from python_scripts.utils import filter_data_maker
from python_scripts.utils import filter_desc_maker
from python_scripts.utils import get_tpl_file
from hashlib import md5


def btn_click(self):
    all_digit = True
    for index, f_blend_str in enumerate(filter_data.blend_mods):
        for each_blend_str in f_blend_str:
            if not each_blend_str.isdigit():
                all_digit = False

    if not all_digit:
        QMessageBox.warning(self, '',
                            'blend格式错误',
                            QMessageBox.Yes)
        return

    for index, f_blend_str in enumerate(filter_data.blend_mods):
        filter_data.blend_modes_num[index] = []
        for each_blend_str in f_blend_str:
            filter_data.blend_modes_num[index].append((int(each_blend_str)))

    check_res = input_check.check(filter_data.filter_id, filter_data.filter_name, filter_data.pics_path,
                                  filter_data.blend_modes_num)
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
        # 生成data文件
        filter_data_maker.data_maker(filter_data.pics_path, filter_data.blend_modes_num)
        # 生成md5
        m5 = md5()
        m5.update(filter_data.filter_data_content.encode('utf-8'))
        # 生成desc文件
        filter_desc_maker.desc_maker(filter_data.filter_id, filter_data.filter_name, m5.hexdigest())
        # 生成滤镜文件
        get_tpl_file.create_file(filter_data.pics_path, filter_data.filter_id)
        # 最后给个toast
        QMessageBox.information(self, '',
                                '生成成功',
                                QMessageBox.Yes)
