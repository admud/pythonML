import pandas as pd
import  quandl

df = quandl.get('WIKI/GOOGL')

# grab the features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]

# high minus low percent change
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0

# daily percent change
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# dataframe for columns that we really want to see
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())
