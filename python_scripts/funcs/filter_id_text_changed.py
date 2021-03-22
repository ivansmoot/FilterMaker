from python_scripts.data import filter_data


def text_changed(self):
    filter_data.filter_id = self.text()
