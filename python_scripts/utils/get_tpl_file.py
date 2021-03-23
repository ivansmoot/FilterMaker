from pathlib import Path
from shutil import rmtree
from zipfile import ZipFile, ZIP_DEFLATED
from os import listdir, path
from python_scripts.data import filter_data

"""
最终生成压缩文件的方法
前提是已经生成了data和desc文件,如果这两个文件不存在,将返回-1
如果图片文件不存在,返回-2
"""


def create_file(pics, filter_id):
    # data和desc要是不存在,就直接返回-1
    if not (Path(Path(filter_data.current_path) / 'template.data').exists() and Path(Path(filter_data.current_path) / 'template.desc').exists()):
        return -1
    # 所有的图片也必须存在
    for pic in pics:
        if not Path(pic).exists():
            return -2
    # 如果需要生成的滤镜文件夹已经存在,就删掉
    if Path(Path(filter_data.current_path) / filter_id).exists():
        rmtree(Path(Path(filter_data.current_path) / filter_id))

    # 创建该文件夹及子文件夹
    Path(Path(Path(filter_data.current_path) / filter_id)).mkdir()
    Path(Path((Path(filter_data.current_path) / filter_id) / 'image')).mkdir()
    Path(Path((Path(filter_data.current_path) / filter_id) / 'raw')).mkdir()

    # 把data和desc移动进去
    (Path(Path(filter_data.current_path) / 'template.data').replace(Path((Path(filter_data.current_path) / filter_id) / (filter_id + '.data'))))
    (Path(Path(filter_data.current_path) / 'template.desc').replace(Path((Path(filter_data.current_path) / filter_id) / (filter_id + '.desc'))))

    # TODO 把图片复制进去,注意是复制,不是移动

    # 如果滤镜文件已存在,先删除
    if Path(Path(filter_data.current_path) / (filter_id + '.tpl')).exists():
        Path.unlink(Path(filter_data.current_path) / filter_id + '.tpl')

    # 调用folder_to_zip生成zip,这里没办法,必须在外面生成zip_file然后传参进去,否则递归的时候就不对了
    # w参数为新建或覆盖,ZIP_DEFLATED是使用gzip算法进行压缩
    zip_file = ZipFile(filter_id + '.tpl', 'w', ZIP_DEFLATED)
    folder_to_zip(zip_file, Path(Path(filter_data.current_path) / filter_id))

    # 生成tpl文件后,把文件夹删了
    rmtree(Path(Path(filter_data.current_path) / filter_id))


def folder_to_zip(zip_file, source_folder):
    # 这里只能调用os的listdir来遍历文件夹下的所有文件和文件夹,pathlib库的那些方法都带有路径名,很扯
    files_and_folders = listdir(source_folder)
    # 遍历所有,如果是文件,就把该文件添加到zip_file里,如果是目录,就递归调用
    for file_or_folder in files_and_folders:
        if path.isfile(Path(source_folder / file_or_folder)):  # 如果是文件
            # 这里要给write,传两个参,不然生成的压缩包里面的文件,会带上完整的路径
            zip_file.write(Path(source_folder / file_or_folder), Path(file_or_folder))
        else:
            zip_file.write(Path(source_folder / file_or_folder), Path(file_or_folder))  # 创建文件夹
            folder_to_zip(zip_file, Path(source_folder / file_or_folder))


if __name__ == '__main__':
    pic_list = [f"C:/Users/ivansmoot/PycharmProjects/filterMaker", ]
    create_file(pic_list, 'filter_id')
