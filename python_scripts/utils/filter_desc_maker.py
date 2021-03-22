def desc_maker(filter_id, filter_name, filter_data_md5):
    # 由于format是通过 { 去实现匹配替换的,但是我们的第一个左花括号是不需要被替换的,所以要再包一层括号,作为转义,而不是使用\进行转义
    # python的坑是真的有点多
    content = '''{{
    "template_fw":1,
    "template_id":{},
    "template_name":{},
    "template_des":{},
    "template_data":{},
    "template_is_encrypt":false,
    "template_data_md5":{}
}}'''
    filter_desc_content = content.format(filter_id, filter_name, filter_name, filter_id + '.data', filter_data_md5)
    # 存文件
    f = open("template.desc", "w")
    f.write(filter_desc_content)
    f.close()


if __name__ == '__main__':
    filter1_id = 'cold1'
    filter1_name = 'cold1_winter'
    filter1_data_md5 = 'e023a82238e0d3321a705b1b9023814e'
    desc_maker(filter1_id, filter1_name, filter1_data_md5)
