import pandas as pd
from toolz.functoolz import compose
import seaborn as sns


class Transform_Util:
    def __init__(self, data):
        self.data = data

    # get index of value that is null
    def get_null_index(self, column):
        return self.data[self.data[column].isnull()].index

    # get index of value that is not null
    def get_not_null_index(self, column):
        return self.data[self.data[column].notnull()].index

    # get index that match with given value
    def get_index_of(self, column, value):
        return self.data[self.data[column] == value].index

    # rename column
    def rename_column(self, column_name, new_name):
        self.data.rename(columns={column_name: new_name}, inplace=True)

    # remove column space
    def delete_column_space(self):
        self.data.columns = self.data.columns.str.strip()

    # data description and info
    #def overview_data(self):
    #    return 'shape of data:' + ''.join(self.data.shape) + '\ndata infomation:\n' \
     #          + ''.join(self.data.info()) + '\ndata describe:\n' + ''.join(self.data.describe())

    # drop data
    def drop_column(self, column_list):
        self.data = self.data.drop(columns=column_list)

    def drop_index(self, index_list):
        self.data = self.data.drop(index=index_list)

    # shift data to fix the values in columns
    def shift_data(self, index, periods, axis, start):
        self.data.iloc[index, start:] = self.data.iloc[index, start:].shift(periods=periods, axis=axis)

    # transform from object type to datetime type
    def to_datetime(self, columns):
        self.data[columns] = pd.to_datetime(self.data[columns], format='%m/%d/%Y %H:%M')

    # transform from object type to string type
    def to_string(self, columns):
        self.data[columns].astype(str)

    # transform from object type to float type
    def to_float(self, columns):
        self.data[columns].astype(str).astype(float)

    # transform from object type to int type
    def to_int(self, columns):
        self.data[columns].astype(str).astype(int)

    # fill data
    def fill_na(self, value, column=None):
        if column == None:
            self.data = self.data.fillna(value)
        else:
            self.data[column].fillna(value, inplace=True)

    def fill_na_distinct(self):
        self.data['price'] = self.data['price'].fillna(int(self.data.mean()))

    # pivot data
    def pivot_data(self):
        return pd.pivot_table(self.data)

    # plot data
    def plot_data(self):
        return None #sns.distplot(day_of_month_landslides, kde=False, bins=31)
