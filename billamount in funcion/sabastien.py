#Let's create a function total_calc() that helps us calculate and print out the total amount paid at a restaurant. Given a bill amount and the percentage of the bill amount you decide to pay us a tip (tip_perc ), this function calculates the total amount you should pay.


def total_calc(bm,tip):
    ctip=tip/100*bm
    totalamount=bm+ctip
    print("the totalamount is ",totalamount)

    
billamount=int(input("enter the bill amount"))
tip=int(input("how much percentage do you want to give a tip?"))

total_calc(billamount,tip)
