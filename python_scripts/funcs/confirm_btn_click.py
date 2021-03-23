from python_scripts.data import filter_data


def btn_click():
    f_id = filter_data.filter_id
    f_name = filter_data.filter_name
    f_pics = filter_data.pics_path
    f_blends = filter_data.blend_mods
    f_btn_names = filter_data.pic_choose_btn_name
    print('id:')
    print(f_id)
    print('name:')
    print(f_name)
    print('pics:')
    print(f_pics)
    print('blends:')
    print(f_blends)
    print('btn names:')
    print(f_btn_names)
