from json import dumps
from python_scripts.data import filter_data
from pathlib import Path


def data_maker(pics, blends):
    """
    研究了一下,由于工具是 图片1-滤镜1、滤镜2、滤镜3 图片2-滤镜1、滤镜2 这样
    但data文件是 滤镜1-图片1、图片2 滤镜2-图片1 这样
    所以传过来的列表格式不能直接使用,需要转化一下
    如传过来的是[[1], [1, 18, 21], [18, 21]],代表第一张图使用了滤镜1,第二张图使用了滤镜1,18,21,第三张图使用了滤镜18,21
    要转换成[[0, 1], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [1, 2], [], [], [1, 2]]
    代表滤镜1(index=0)有图片1(index=0)和图片2(index=1)使用
    滤镜18(index=17)有图片2(index=1)和图片3(index=2)使用
    这样确实会浪费点空间,但是具有扩展性,因为据说下个版本会支持1-21的所有滤镜
    """
    from_blend_to_find_pic = [[] for _ in range(21)]

    # 存放滤镜data文件的resources和filters字段
    resources = []
    filters = []

    # 进行列表转换
    for index, blend in enumerate(blends):
        for each_blend in blend:
            from_blend_to_find_pic[int(each_blend - 1)].append(index)

    # 动态生成resources结构
    for index, pic in enumerate(pics):
        if str(pic).split('.')[-1] == 'acv':
            res_type = 'acv'
        else:
            res_type = 'drawable'
        res_path = 'image/' + str(pic).split('/')[-1]
        resources.append({
            "res_id": index + 1,
            "res_type": res_type,
            "res_name": str(pic).split('/')[-1],
            "res_path": res_path
        })

    # filter里面会有多种滤镜效果
    filter_id_num = 0
    for index, b2p in enumerate(from_blend_to_find_pic):
        if b2p:  # 如果是空的,代表该滤镜不对任何图片生效,跳过即可
            input_content = []
            in_id_num = 0
            for each_b2p in b2p:
                input_content.append(filter_data.get_input_content(each_b2p + 1, index + 1, in_id_num + 1))
                in_id_num += 1
            filters.append({
                "filter_id": filter_id_num + 1,
                "filter_type": index + 1,
                "inputs": input_content
            })
            filter_id_num += 1

    # 最终的JSON其实就这三个字段,主要是resources和filters里面有嵌套的
    filter_data_dict = {
        "version": 1,
        "resources": resources,
        "filters": filters
    }

    # 根据dict生成一个JSON,indent代表四个空格来格式化separators是指用逗号和冒号空格来隔开,主要是为了冒号后面那个空格,看起来好看点
    filter_data_content = dumps(filter_data_dict,ensure_ascii=False, indent=4, separators=(',', ': '))

    # 存文件
    f = open(Path(filter_data.current_path) / "template.data", "w")
    f.write(filter_data_content)
    f.close()

    # 存公共变量
    filter_data.filter_data_content = filter_data_content
