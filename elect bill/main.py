#Write a program to calculate the electricity bill. The bill is calculated by checking the number of units consumed. Suppose the user is consuming less than 50 units. The per-unit cost will be 2.60, and the tax on that bill will be 25. If a user is consuming more than 50 but less than 100. Then the per-unit cost will be 3.25, and the tax on that bill will be 35 If the user is coming more than 100 and less than 200. Then the per-unit cost will be 5.26, and the tax will be 45 And above 200, the cost of the unit is 8.45, and the tax is 75.
units=int(input("enter how much unit consumed"))

if units<50:
    totalcost=units*2.60
    tax=25
elif units>50 and units<100:
    totalcost=units*3.25
    tax=35
elif units>100 and units<200:
    totalcost=units*5.26
    tax=45
else:
    totalcost=units*8.45
    tax=75

print("the electricity bill is ",totalcost+tax)