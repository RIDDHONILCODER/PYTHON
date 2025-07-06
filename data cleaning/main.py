import numpy as np
import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt

df=pd.read_csv('country_vaccinations.csv')
print(df.head())
#checking null values
print(df.isnull().sum())
#chicking na values
missings_values=["N/a","na",np.nan]
df=pd.read_csv('country_vaccinations.csv',na_values=missings_values)
print(df.isnull().sum())
print("checking if there is any null values ",df.isnull().any())
print("The no of rows are ",df.shape)
subset=df.iloc[:100]
sb.heatmap(subset.isnull(),annot=True)
plt.show()
df.dropna()