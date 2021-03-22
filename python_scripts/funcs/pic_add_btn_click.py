from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QWidget
from python_scripts.funcs import pic_choose_btn_click
from python_scripts.data import filter_data


# 点击该按钮,动态增加一个按钮和一个输入框,满足多张图片输入的需求
# 目前遇到的一个问题是,动态新增的按钮需要在最下面,不然不知道怎么把下面已存在的按钮刷新至最下方,只加一排是可以的,再加就不行了
def btn_click(self, grid):
    names = locals()
    # 按钮的名称和位置都是根据全局变量total_row生成的
    btn_name = 'pic_choose_btn' + str(filter_data.total_row - 1)
    edit_name = 'filter_choose_edit_combine_btn' + str(filter_data.total_row - 1)

    names[btn_name] = QPushButton('选择一张图片')
    names[btn_name].clicked.connect(lambda: pic_choose_btn_click.btn_click(self, filter_data.total_row - 3))

    names[edit_name] = QLineEdit()
    names[edit_name].setMaxLength(20)
    names[edit_name].setPlaceholderText('请输入混合模式')

    grid.addWidget(names[btn_name], filter_data.total_row - 1, 0)
    grid.addWidget(names[edit_name], filter_data.total_row - 1, 1)
    QWidget.setFont(names[btn_name], QFont("STSong"))
    QWidget.setFont(names[edit_name], QFont("STSong"))

    # 每增加一行,总行数就加一
    filter_data.total_row += 1
    # 并且pics_path也增加一个空值,由于input_check也会检查空值,所以也没啥问题
    filter_data.pics_path.append('')
