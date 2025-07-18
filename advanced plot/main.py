import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('Iris Dataset.csv')
print(df.columns)

x=df['Species']
y=df['SepalLengthCm']

plt.bar(x,y)
plt.xlabel("Species")
plt.ylabel("SepalLengthCm")
plt.show()