import pandas as pd 
import seaborn as sms
import matplotlib.pyplot as plt
df=pd.read_csv("USA_Housing.csv")
print(df.head())
print("the name of the column ",df.info())
print(df.describe())
sms.distplot(df["Area Population"])
plt.show()