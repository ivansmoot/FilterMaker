from os import path
from sys import argv


# 设置几个全局变量
total_row = 3  # ui的总行数
filter_id = ''  # 保存滤镜id
filter_name = ''  # 保存滤镜name
pics_path = ['']  # 保存选择的图片
blend_mods = [[]]  # 保存每张图需要应用的滤镜
blend_modes_num = [[]]  # 以数字的形式存滤镜
pic_choose_btn_name = ['请选择一张图片']  # 保存每个图片选择按钮的名称,因为这个按钮的名称会动态修改
support_blend_formats = [1, 18, 21]  # 目前支持的滤镜有这些
support_pic_formats = ['png', 'jpeg', 'jpg', 'acv']  # 目前支持的图片格式
filter_data_content = ''  # 存data数据,方便生成md5
current_path = path.dirname(path.realpath(argv[0]))  # 当前目录获取巨坑,还得要这样搞


# 动态生成filters结构
# 传三个参数,分别是这个滤镜是对哪张图片生效的,哪种blend效果,以及这是该效果里的第几个(因为一个效果可能被应用到多张图片上)
def get_input_content(pic_id, blend_num, in_id):
    content = {
        1: {
            "in_id": in_id,
            "in_type": "uniform",
            "in_data_name": "inputImageTexture2",
            "in_data_value": "3",
            "in_data_size": 1,
            "in_data_type": "sample2D",
            "in_source_type": 1,
            "in_source_res_id": pic_id,
            "in_source_filter_id": 0
        },
        18: {
            "in_id": in_id,
            "in_type": "uniform",
            "in_data_name": "inputImageTexture2",
            "in_data_value": "3",
            "in_data_size": 1,
            "in_data_type": "sample2D",
            "in_source_type": 1,
            "in_source_res_id": pic_id,
            "in_source_filter_id": 0
        },
        21: {
            "in_id": in_id,
            "in_type": "uniform",
            "in_data_name": "inputImageTexture2",
            "in_data_value": "3",
            "in_data_size": 1,
            "in_data_type": "sample2D",
            "in_source_type": 1,
            "in_source_res_id": pic_id,
            "in_source_filter_id": 0
        }
    }
    return content.get(blend_num, None)
