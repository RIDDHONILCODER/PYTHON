#Write a program to create a class Computer with a private attribute max_price and methods sell(to display) the selling price and setmaxprice(change the private attribute max_price). Now create an object for the class Computer. Try changing the value of max price and use the sell function to display the updated price. Use a setter function to update the value and again display the price.
class computer:
    __max_price=1000
    def sell(self):
        print("the selling price is ",computer.__max_price)
    def setmaxprice(self,price):
        computer.__max_price=price
        print("the new price is this ",computer.__max_price)

ob=computer()
ob.setmaxprice(2000)
