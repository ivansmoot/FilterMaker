import base64


# 将图片转成base64,存在一个文件里
# 之所以搞这么麻烦而不是直接用图片,是因为pyinstaller不能把图片打到执行文件里,只能搞出个文件来
def pic_to_py(pictures_path, py_name):
    write_data = []
    for picture_path in pictures_path:
        # 每张图的存放格式是 图片名 = ""
        # 这边先拿到图片名,注意要去掉路径的部分和图片后缀的部分
        picture_name = str(picture_path).split('/')[-1].split('.')[0]
        open_pic = open(picture_path, 'rb')
        b64str = base64.b64encode(open_pic.read())
        open_pic.close()
        # 注意这边b64str一定要加上.decode()
        write_data.append('%s = "%s"\n' % (picture_name, b64str.decode()))

    f = open(py_name + '.py', 'w+')
    for data in write_data:
        f.write(data)
    f.close()


# 读取某个base64的图片
def get_pic(pic_code, pic_name):
    image = open(pic_name, 'wb')
    image.write(base64.b64decode(pic_code))
    image.close()


if __name__ == '__main__':
    pics = ["../../res/images/questionMark.png", "../../res/images/main.icns"]
    pic_to_py(pics, 'pics_in_base64')  # 将pics里面的图片写到 memory_pic.py 中
