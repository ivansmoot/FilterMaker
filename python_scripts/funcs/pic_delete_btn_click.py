from python_scripts.data import filter_data
from sip import delete


def btn_click(grid):
    # 删除最后的一个按钮和一个文本输入框
    # 先找到这个文本框
    last_blend_edit = grid.itemAt(8 + (filter_data.total_row - 3) * 2).widget()
    # 删除方法
    grid.removeWidget(last_blend_edit)
    delete(last_blend_edit)

    # 找到按钮
    last_pic_button = grid.itemAt(7 + (filter_data.total_row - 3) * 2).widget()
    # 删除
    grid.removeWidget(last_pic_button)
    delete(last_pic_button)

    # 删除后相应的值要被删除
    filter_data.total_row -= 1
    filter_data.pics_path.pop()
    filter_data.blend_mods.pop()
    filter_data.pic_choose_btn_name.pop()
