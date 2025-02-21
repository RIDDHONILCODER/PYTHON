#First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.
my_dictionary={'id1':{'name':'riddhonil','class':5,'subject':['english,maths,sience,bangla']},
               'id2':{'name':'amaar','class':5,'subject':['english,maths,sience']},
               'id3':{'name':'sonali','class':5,'subject':['english,maths,bangla']}
              }
for key,values in my_dictionary.items():
    print("key= ",key)
    print("value= ",values)

