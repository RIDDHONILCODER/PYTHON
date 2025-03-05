my_list=[1,2,36,34,68,58]
even_list=[x for x in my_list if x %2==0]
print("the even list is ",even_list)

my_dict={str(x):x+x for x in my_list}
print("the dict is ",my_dict)

#adding 2 diffrent list
my_list1=[12,23,34,45,56,67,78]
result=map(lambda x,y:x+y,my_list,my_list1)
result=list(result)
print("the addition of the list is  ",result)
def square(x):
    return x*x

#finding square of my_list
result=map(square,my_list)
result=list(result)
print("the square of my list is ",result)
#zip 2 list 
name=['riddhonil','messi','ronaldo']
score=[3,4,10]
result=zip(name,score)
result=list(result)
print("the zip list is this ",result)
