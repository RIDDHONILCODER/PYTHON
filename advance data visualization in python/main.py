import pandas as pd 
import seaborn as sms
import matplotlib.pyplot as plt


df=pd.read_csv("weather.csv")
print(df.info())
#create a bar graph
sms.barplot(df,x='wind_speed',y='temperature',hue='weather_type')
sms.displot(df['temperature'])
sms.pairplot(df[['humidity','temperature','air_pollution_index']])
plt.show()