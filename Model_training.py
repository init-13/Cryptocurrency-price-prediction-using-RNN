import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = pd.read_csv('C:/Users/Debian_Boy/OneDrive/Desktop/BTC_data/BTC-2021min.csv', date_parser = True)
data.tail()
#print(data)
#data training
data_training = data[data['date']< '2022-02-22 05:02:00'].copy()
print(data_training)


