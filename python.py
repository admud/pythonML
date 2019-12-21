import pandas as pd
import  quandl
import math

df = quandl.get('WIKI/GOOGL')

# grab the features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

# high minus low percent change
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# dataframe for columns that we really want to see
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

# change to what you want to predict/forecast
forecast_col = 'Adj. Close'

# fill in missing data, as the algo cannot take in not a number
df.fillna(-99999, inplace =True)

# rounds up the value, using data from 10 days out?
forecast_out = int(math.ceil(0.01*len(df)))

# shifting column up
df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace = True)
print(df.head())
print("Alan")
