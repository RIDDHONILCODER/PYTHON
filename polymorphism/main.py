#Write a program to create two classes for two different countries that consist of three methods to display the following information of respective country - capital, language and type of country. Then, use Polymorphism to create a common interface for both classes.
class india():
    def capital(self):
        print("the capital of india is delhi")
    def language(self):
        print("india has many languages")
class bangladesh():
    def capital(self):
        print("the capital of bangladesh is dhaka")
    def language(self):
        print("bangladesh has many languages")
        
ob1=india()
ob2=bangladesh()
for i in (ob1,ob2):
    i.capital()
    i.language()
    
