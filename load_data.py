import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# load the dataset
df = pd.read_csv('bitcoin_sample_data.csv')

# isplay the first few rows of the dataset
#print(df.head())
#calculate the average (mean), median, and standard deviation of Bitcoin prices.
#print(f"standard deviation is {df['Close'].std()}")
#print(df.max())
#print(df.min())
#print(df['Low'].min())
#print(df[df['Low'] == df['Low'].min()])

"""df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(10, 6)) 
plt.plot(df['Date'],df['Close'])

ax = plt.gca()
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) 

plt.gcf().autofmt_xdate() 
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Stock Price Over Time')

plt.show()"""

#print(df['Close'].shift(1))

daily_dif = df['Close']-(df['Close'].shift(1))

#print(daily_dif)

for value in daily_dif:
    if value < 0:
        print(f"price decrease of {value}")
    else:
        print(f"price increase of {value}")
  

plt.figure(figsize=(10, 6)) 
plt.hist(daily_dif, bins=20, color='blue', edgecolor='black')

ax = plt.gca()

plt.gcf().autofmt_xdate() 
plt.xlabel('difference')
plt.ylabel('frequency')
plt.title('daily differences of BTC')

plt.show()
