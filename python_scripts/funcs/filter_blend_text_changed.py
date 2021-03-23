from python_scripts.data import filter_data


def text_changed(self, index):
    filter_data.blend_mods[index] = []
    for each_blend in str(self.text()).split(' '):
        filter_data.blend_mods[index].append(each_blend)
