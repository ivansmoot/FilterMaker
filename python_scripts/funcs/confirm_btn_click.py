from python_scripts.data import filter_data


def btn_click():
    f_id = filter_data.filter_id
    f_name = filter_data.filter_name
    f_pics = filter_data.pics_path
    f_blends = filter_data.blend_mods
    print(f_id)
    print(f_name)
    print(f_pics)
    print(f_blends)
