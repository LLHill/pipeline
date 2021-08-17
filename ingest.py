import pandas as pd
import os

class Ingest:
    def __init__(self,src):
        self.src = src

    def ingest_from_csv(self, encoding=None):
        return pd.read_csv(self.src, encoding=encoding)

    def ingest_from_html(self, encoding=None):
        return pd.read_html(self.src, encoding=encoding)

    def ingest_from_json(self, encoding=None):
        return pd.read_json(self.src, encoding=encoding)

    def ingest_from_excel(self, encoding=None):
        return pd.read_excel(self.src, encoding=encoding)

    def ingest(self, encoding):
        print('ingesting...')
        file_path, extension = os.path.splitext(self.src)
        if (extension == '.csv'):
            return self.ingest_from_csv(encoding)
        elif (extension == '.html'):
            return self.ingest_from_html(encoding)
        elif (extension == '.xlsx'):
            return self.ingest_from_excel(encoding)
        elif (extension == '.json'):
            return self.ingest_from_json(encoding)
        else:
            raise Exception('Not support for this file type')
