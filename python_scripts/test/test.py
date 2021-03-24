from os import sep, path, walk
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def folder_to_zip(source_folder):
    zip_name = str(source_folder).split('/')[-1] + '.zip'
    zip_file = ZipFile(zip_name, 'w', ZIP_DEFLATED)
    for base_path, dir_names, file_names in walk(source_folder):
        inner_path = base_path.replace(str(source_folder), '')  # 这一句很重要，不replace的话，就从根目录开始复制
        if inner_path != '':
            inner_path += sep
        for filename in file_names:
            zip_file.write(path.join(base_path, filename), inner_path + filename)
    zip_file.close()


if __name__ == '__main__':
    folder_to_zip(Path('/Users/containermachine/Desktop/test'))
