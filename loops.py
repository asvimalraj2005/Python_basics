#There are two types of loop in python language namely
# --for loop-- :: Syntax            for( entry value ,exit value , increment/decrement ):
# --while loop-- :: Syntax              while( boolean condition ):


# for loop is an entry loop
# while loop is an exit loop

#Examples for  --for loop--

#simple example

for i in range(0):
    print("Hello World")


# range keyword is an inbuilt python function

for i in range(10):
    print(i,end='')

# The above example is for printing 0 to 9 by using range function 
# i is an keyword which is specified for row 
# so we are printing the printing the values from 0 to 9 by using i variable with range function

# The output for the above program is 0123456789
# Without using  ---  end='' --- keyword we can able to get the output as 
#0
#1
#2
#3
#4
#5
#6
#7
#8
#9

# The same output can we get by using while loop as well
i=0
while(i>10):
    print(i)           #while conditional is used rarely in real world use cases
    i=i+1

# i is an variable which is initialized as the value as 0
# while is an inbuilt python looping keyword 
# i>10 is an boolean keyword which stops the looping process until the previous value of 10
# i=i+1 is an increment function which is used to increment the values 

#we can able to use for loop for iterating the values in list,dictionaries,and tuples

#example 
list1=[1,2,4,5,7,89]
for val in list1:
    print(val)

# list1 is an list variable's name which contains the values within square brackets 
# Using for loop we can easily able to traverse the items in the list
# for val in list1: --- val in list --- the variable val traverse the n of items in the given list by using for loop 
# We can print the values in the list by using val keyword


#another example 

# we can able to use two keywords inside the for loop function
list2=[1,2,3,4,5,6,7,8]
for index,val in enumerate(list2):
    print("The index is ", index ," and the values is " ,val)


#index word is used to iterate(indexing the values) the items inside in an given list by using their index val with enumerate function
#val word is used to traverse(accessing the values) the items inside an list by using enumerate function
# index variable stores the index of the objects(values inside the list2
# list2[val] , val is an keyword which traverse the items in list2 

#loop using dictionaries 

dict1={"key_1":"value_1","key_2":"value_2","key_3":"value_3"}
for key,value in dict1.items():
    print("The key is ",key," and the value is ",value)

# we are declaring the key , value keyword inside an loop binded with dict1.items()
# key variable stores the keys inside an dict1
# value variable stores the values inside an dict1
# items() is an python inbuilt dictionary keyword which can able to access both the keys and values inside an given dictionary

for key in dict1.keys():
    print("The keys inside the dictionary1 is",key)

# keys() is an python inbuilt dictionary keyword which is used to access the key variables of the given dictionary
# key is an user-defined variable which is used to store key elements that is associated with the value elements

for value in dict1.values():
    print("The values in the dictionary is ",value)

# values() is an python inbuilt dictionary function keyword which is used to access the values inside an given dictionary by using for loop
# value is an user-defined variable which is used to store the values elements which is associated with key elements



#dictionary is mutable like list, but we can iterate the values inside in an tuple but we can't change em
