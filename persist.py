import pandas as pd

class Persist:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def save(self, extension, file_name):
        print('saving....')
        if extension == '.csv':
            return self.save_to_csv(file_name)
        elif extension == '.xlsx':
            return self.save_to_excel(file_name)
        else:
            raise Exception('Unsupported format')

    def save_to_csv(self, file_name):
        self.data.to_csv(f'{self.path}\\{file_name}.csv')

    def save_to_excel(self, file_name):
        self.data.to_excel(f'{self.path}\\{file_name}.xlsx')