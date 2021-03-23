from re import match
from python_scripts.data import filter_data

"""
check函数接受四个参数,分别是滤镜id,滤镜name,滤镜使用的图片,以及每张图片使用的blend
该函数只做判断校验参数是否合法使用,
返回值:
-1: 参数类型不对,四个参数的类型分别需要是str,str,list,list
-2: id或name参数有空的情况
-3: id不符合规则,需要是字母或下划线开头,后面可以有数字,第一位不能是数字
-4: pics或blends给的不对,可能是空,或里面含空
-5: pics里存在错误数据,如不支持格式的文件,或存在重复的文件
-6: blends里存在错误数据,如不支持的滤镜数字
"""


def check(filter_id, filter_name, pics, blends):
    # 基本类型必须符合要求
    if not (isinstance(filter_id, str) or isinstance(filter_name, str)
            or isinstance(pics, list) or isinstance(blends, list)):
        return -1
    # id和name都不能为空
    if filter_id.strip() == '' or filter_name.strip() == '':
        return -2
    # id要符合格式要求
    if not match(f'^[a-zA-Z_][0-9a-zA-Z_]*$', filter_id):
        return -3
    # pics和blends不能为空数组
    if (not pics) or (not blends):
        return -4
    # pics数组的每一项都必须是非空的str,全是空格也不行
    for pic in pics:
        if not (isinstance(pic, str) and pic.strip() != ''):
            return -4
    # blends的每一项都必须是个list,每个list的每一项都必须是数字
    for blend in blends:
        if not (isinstance(blend, list)):
            return -4
        else:
            for each_blend in blend:
                if not isinstance(each_blend, int):
                    return -4
    if len(pics) != len(blends):
        return -4
    # pics的每一项都必须是支持图片格式的结尾
    for pic in pics:
        pic_format = str(pic).split('.')[-1]
        if pic_format not in filter_data.support_pic_formats:
            return -5
    # pics不能重复
    pics_set = set(pics)
    if len(pics_set) != len(pics):
        return -5
    # blend的每一项的每个数字都需要是支持的滤镜格式
    for blend in blends:
        for each_blend in blend:
            if each_blend not in filter_data.support_blend_formats:
                return -6
    else:
        return 1


if __name__ == '__main__':
    filter1_id = 'cold1'
    filter1_name = 'cold1_winter'
    pic_list = ['/user/bin/pic1.png', '/user/images/pic2.jpeg', './pic3.acv']
    lends_list = [[1], [1, 18, 21], [18, 21]]
    print(check(filter1_id, filter1_name, pic_list, lends_list))
