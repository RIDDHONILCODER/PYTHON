import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('Countries Data.csv')
c_52=df.loc[df['year']==1952]
c_2007=df.loc[df['year']==2007]
#marging the data of line 1952 and 2007
df1=c_52.merge(c_2007,right_on='country',left_on='country')
df2=df1.head(7)
x=df2['population_x']
print(x)
plt.bar(df2['country'],df2['population_x'],width=0.5,color="blue")
plt.show()
