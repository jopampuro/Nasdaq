from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from click._compat import raw_input
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np

data = pd.read_csv("../Nasdaq/tickersinfo.csv") #data set limpio
\
class TechnicalIndicators:
    def __init__(self):
        self.api_key= "b"
        self.macd_data=self.macd()
        self.bbands_data=self.bbands()
    def macd(self):
        a = TechIndicators(key=self.api_key, output_format='pandas')
        data, meta_data=a.get_macd(symbol=self.stock_name,interval='daily')
        return data
    def bbands (self):
        c=TechIndicators(key=self.api_key,output_format='pandas')
        data,meta_data=c.get_bbands(symbol=self.stock_name)
        return data
 def question(self):
        stock_name=raw_input("Stock Name")
        return stock_name
