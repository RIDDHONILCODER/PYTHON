#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}.
dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
count=0
for key,value in dict.items():
    if value==2:
        count=count+1
print("the frequency of the value 2 is ",count)
#Write a program to return the country code for various countries. Here’s a dictionary of different country codes - {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}.
country_dict={'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}
print("the code for country nepal is ",country_dict['Nepal'])
print("the code for country bangladesh is ",country_dict.get('bangladesh','not found'))
