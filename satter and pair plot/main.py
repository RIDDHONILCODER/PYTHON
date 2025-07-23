import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
df=pd.read_csv("USA_Housing.csv")
print(df.columns)
sb.pairplot(df)
plt.show()

sb.heatmap(df.drop('Address',axis=1).corr(),annot=True)
plt.show()
