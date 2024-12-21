num=int(input("enter a number"))
#checking if the number is positive or not
if num>0:
    print(num," is positive.")
else:
    print(num,"is'nt positive")

#Write to check if a person is buying oranges at 100 rs and later selling it 1at 120 rs. Find that he has profit or loss?

sellingprice=80
costprice=100

if sellingprice>costprice:
    profit=sellingprice-costprice
    print("i am selling at a profit of ",profit)
else:
    print("i am selling at a loss")