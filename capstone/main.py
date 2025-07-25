import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sb
df=pd.read_csv('heart.csv')
#print(df.isnull().sum())
#creating a heat map
plt.figure(figsize=(20,10))
#sb.heatmap(df.corr(),annot=True,cmap='terrain')
#sb.pairplot(df)
#df.hist(figsize=(20,10))
sb.barplot(df,x='sex',y='chol',palette='spring')
plt.show()