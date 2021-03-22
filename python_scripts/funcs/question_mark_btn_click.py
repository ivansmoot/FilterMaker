from PyQt5.QtWidgets import QMessageBox, QWidget


def btn_click(self):
    # 这玩意不让改字体
    QMessageBox.information(self, '',
                            '目前支持的混合模式:\n'
                            '查色表(1),柔光(18),线性减淡(21),\n'
                            '请输入需要设置的效果并以空格分开，\n'
                            '如: 1 18 21',
                            QMessageBox.Yes)
