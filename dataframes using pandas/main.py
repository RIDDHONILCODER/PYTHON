import pandas

dict={
    "cars":["lamborgini sesto","porshe 911","mercedes e class","toyota supra mk5"],
    "hobby":["Gaming","cycling","coding","playing uno"]
}
ind=['a','b','c','d']
df=pandas.DataFrame(dict,index=ind)
print(df)

num=[23,45,67,1,2,3]
print(pandas.Series(num))

