

from abc import ABC,abstractmethod
#creating base class
class abc(ABC):
    def display_value(self,x):
        print("the value is this ",x)
    @abstractmethod
    def task(self):
        print("inside the abstract method")
class xyz(abc):
    def task(self):
        print("inside the sub class")
ob=xyz()
ob.display_value(567)
ob.task()