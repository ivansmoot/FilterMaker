from python_scripts.data import filter_data


def text_changed(self, index):
    filter_data.blend_mods[index] = self.text()
