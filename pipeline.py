# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
from ingest import Ingest
from transform.transform import Transform
from persist import Persist
class Pipeline:
    def run(src):
        #ingesting
        ingest = Ingest(src)
        ingested_data = ingest.ingest('ISO-8859-1')

        #transforming
        transform = Transform(ingested_data)
        #start process
        transformed_data = transform.process()
        #overview_info = transform.overview_data()

        #persisting
        persist = Persist(transformed_data, 'DataHouse')
        persist.save('.csv','ks_transformed_data')

