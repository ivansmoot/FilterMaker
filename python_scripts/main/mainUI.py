from sys import argv, exit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from python_scripts.funcs import pic_choose_btn_click
from python_scripts.funcs import question_mark_btn_click
from python_scripts.funcs import pic_add_btn_click
from python_scripts.funcs import confirm_btn_click
from python_scripts.funcs import filter_name_text_changed
from python_scripts.funcs import filter_id_text_changed
from python_scripts.funcs import filter_blend_text_changed
from python_scripts.utils import pics_in_base64
from python_scripts.utils import pic2py
from python_scripts.data import filter_data


class MainUI(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 设置网格布局
        grid = QGridLayout()
        self.setLayout(grid)
        self.setWindowTitle('滤镜制作')  # 设置标题

        filter_id_edit = QLineEdit()
        filter_id_edit.setMaxLength(20)
        filter_id_edit.setPlaceholderText('请输入滤镜id')
        # 只要文本框的内容一变,就立即更新filter_data里存放的值
        filter_id_edit.textChanged.connect(lambda: filter_id_text_changed.text_changed(filter_id_edit))
        grid.addWidget(filter_id_edit, 0, 0)

        filter_name_edit = QLineEdit()
        filter_name_edit.setMaxLength(20)
        filter_name_edit.setPlaceholderText('请输入滤镜name')
        filter_name_edit.textChanged.connect(lambda: filter_name_text_changed.text_changed(filter_name_edit))
        grid.addWidget(filter_name_edit, 0, 1)

        # 创建按钮,绑定事件,设置位置tt
        # 这里有个坑是按钮点击事件方法,在另一个文件里,要用lambda才行
        pic_choose_btn_add_one = QPushButton('+')
        pic_choose_btn_add_one.clicked.connect(lambda: pic_add_btn_click.btn_click(self, grid))
        grid.addWidget(pic_choose_btn_add_one, 0, 2)

        pic_choose_btn_delete_one = QPushButton('-')
        grid.addWidget(pic_choose_btn_delete_one, 0, 3)

        pic_choose_btn1 = QPushButton(filter_data.pic_choose_btn_name[0])
        pic_choose_btn1.clicked.connect(lambda: pic_choose_btn_click.btn_click(self, 0, pic_choose_btn1))
        grid.addWidget(pic_choose_btn1, 1, 0)

        filter_choose_edit_combine_btn1 = QLineEdit()
        filter_choose_edit_combine_btn1.setMaxLength(20)
        filter_choose_edit_combine_btn1.setPlaceholderText('请输入混合模式')
        filter_choose_edit_combine_btn1.textChanged.connect(lambda: filter_blend_text_changed.text_changed(filter_choose_edit_combine_btn1, 0))
        grid.addWidget(filter_choose_edit_combine_btn1, 1, 1)

        explain_filters_which_support = QPushButton()
        # 通过base64读出一张图
        pic2py.get_pic(pics_in_base64.questionMark, 'question_mark_decode_in_base64')
        # 设置该按钮的icon
        explain_filters_which_support.setIcon(QIcon("question_mark_decode_in_base64"))
        # 设置按钮无边框，不然很难看
        explain_filters_which_support.setStyleSheet("border:none;")
        # 让按钮居左一点，离文本框近一点
        explain_filters_which_support.setFixedWidth(20)
        explain_filters_which_support.clicked.connect(lambda: question_mark_btn_click.btn_click(self))
        grid.addWidget(explain_filters_which_support, 1, 2)

        cancel_btn = QPushButton('取消')
        # 设置该按钮的点击事件为关闭窗口
        cancel_btn.clicked.connect(QCoreApplication.instance().quit)
        grid.addWidget(cancel_btn, 1, 3)

        confirm_btn = QPushButton('确定')
        confirm_btn.clicked.connect(lambda: confirm_btn_click.btn_click())
        grid.addWidget(confirm_btn, 1, 4)

        # 拿到屏幕的大小,算中心点,让这个窗口在屏幕中间,而不是写死一个值
        # 但是目前看上去有点歪了,具体原因待排查
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))

        # 设置所有字体,注:只对当前已经生成的文字生效,动态生成的要重新设置字体
        self.setFont(QFont("STSong"))
        self.show()


if __name__ == '__main__':
    app = QApplication(argv)
    # 设置在程序坞里的图标
    pic2py.get_pic(pics_in_base64.main, "main_decode_in_base64")
    app.setWindowIcon(QIcon("main_decode_in_base64"))
    ex = MainUI()
    exit(app.exec_())
