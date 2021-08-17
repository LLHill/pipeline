import pandas as pd
from toolz.functoolz import compose
import transform.transform_util
import seaborn as sns


class Transform:
    def __init__(self, transform_util):
        self.transform_util = transform_util

    # start transform function
    def process(self):
        self.pipeline_transform()
        return self.transform_util.data

    # Adjust the pipeline
    def pipeline_transform(self):
        return compose(self.transform_util.delete_column_space(),
                       self.transform_util.rename_column('temp', 'ID'),
                       self.transform_util.fill_na('No name', 'name'),
                       self.transform_util.shift_data(self.transform_util.get_null_index('category'), -1, 1, 2),
                       self.transform_util.shift_data(self.transform_util.get_not_null_index('Unnamed: 16'), -4, 1, 2),
                       self.transform_util.shift_data(self.transform_util.get_not_null_index('Unnamed: 15'), -3, 1, 2),
                       self.transform_util.shift_data(self.transform_util.get_not_null_index('Unnamed: 14'), -2, 1, 2),
                       self.transform_util.shift_data(self.transform_util.get_not_null_index('Unnamed: 13'), -1, 1, 2),
                       self.transform_util.drop_column(['Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16']),
                       self.transform_util.shift_data(self.transform_util.get_index_of('deadline', 'USD'), -1, 1, 4),
                       self.transform_util.shift_data(self.transform_util.get_index_of('usd pledged', 'N,"0'), -1, 1, 4),
                       #self.data[['usd pledged', 'goal', 'pledged', 'backers']].apply(self.to_float, axis=1),
                       self.transform_util.to_float('usd pledged'),
                       self.transform_util.to_float('goal'),
                       self.transform_util.to_float('pledged'),
                       self.transform_util.to_float('backers'),
                       self.transform_util.to_datetime('deadline'),
                       self.transform_util.to_datetime('launched')
                       )
