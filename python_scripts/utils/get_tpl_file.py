from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile, ZIP_DEFLATED
from os import path, sep, walk
from python_scripts.data import filter_data
from shutil import copyfile
from re import match

"""
最终生成压缩文件的方法
前提是已经生成了data和desc文件,如果这两个文件不存在,将返回-1
如果图片文件不存在,返回-2
"""


def create_file(pics, filter_id):
    # data和desc要是不存在,就直接返回-1
    if not (Path(filter_data.current_path, 'template.data').exists() and Path(filter_data.current_path, 'template.desc').exists()):
        return -1
    # 所有的图片也必须存在
    for pic in pics:
        if not Path(pic).exists():
            return -2
    # 如果需要生成的滤镜文件夹已经存在,就删掉
    if Path(filter_data.current_path, filter_id).exists():
        rmtree(Path(filter_data.current_path, filter_id))

    # 创建该文件夹及子文件夹
    Path(filter_data.current_path, filter_id).mkdir()
    Path(filter_data.current_path, filter_id, 'image').mkdir()
    Path(filter_data.current_path, filter_id, 'raw').mkdir()

    # 把data和desc移动进去
    Path(filter_data.current_path, 'template.data').replace(Path(filter_data.current_path, filter_id, filter_id + '.data'))
    Path(filter_data.current_path, 'template.desc').replace(Path(filter_data.current_path, filter_id, filter_id + '.desc'))

    # 把图片复制进去,注意是复制,不是移动
    for pic in filter_data.pics_path:
        copyfile(Path(pic), Path(filter_data.current_path, filter_id, 'image', str(pic).split('/')[-1]))

    # 如果滤镜文件已存在,先删除
    if Path(filter_data.current_path, filter_id + '.tpl').exists():
        Path.unlink(Path(filter_data.current_path, filter_id + '.tpl'))

    # 最后的压缩
    folder_to_zip(Path(filter_data.current_path) / filter_id)

    # 生成tpl文件后,把文件夹删了
    rmtree(Path(filter_data.current_path, filter_id))


def folder_to_zip(source_folder):
    # 压缩包名称
    zip_name = str(source_folder).split('/')[-1] + '.tpl'
    # 生成一个ZipFile
    # 这里一定要注意ZipFile的路径,不然打包后可能生成在错误的位置
    zip_file = ZipFile(Path(filter_data.current_path, zip_name), 'w', ZIP_DEFLATED)
    # os的walk方法真香
    for base_path, dirs, files in walk(source_folder):
        # 这里的inner_path是指这个文件/文件夹,相对于被压缩的最外面的文件夹的路径,而不是相对于根目录,这个很重要
        inner_path = base_path.replace(str(source_folder), '')
        if inner_path != '':
            inner_path += sep
        # 文件夹也要单独加一下,不然空文件夹就没了
        for each_dir in dirs:
            zip_file.write(Path(base_path, each_dir), inner_path + each_dir)
        for each_file in files:
            # 隐藏文件就算了,mac真的垃圾
            if not match(each_file, r'^\..*$'):
                zip_file.write(Path(base_path, each_file), inner_path + each_file)
    zip_file.close()
