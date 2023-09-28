# In python language there are total two if conditional branching statements
# namely , simple if-else statement , conditional braching nested if elif else statement

#example for simple if-else statement

# if(condition):
    #if the given input satisfies the if boolean condition then the statement in this is block will be executed
    #if the given input condition does not satisfies the if condition then the statements inside the if block will be skipped and the else statement block will be executed
# else:
    #The statement inside the else block will be executed if the given condition does not satisfies the if boolean condition

#Example 1

user_input=int(input("Enter the age to check your eligiblitiy of voting"))
if (user_input<18):
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")


# by using user_input variable we are storing the user input value in to it
# only in the if block the boolean conditions can be initialized not in else block
# explanation
# if(user_input<18): --->> user_input < 18 means if the user is less than the age of 18 than the user will credited as you are not eleigible to vote
# if he is above 18 than the if part will be skipped as the if block contains an boolean condition , the boolean condition acts as a gate ,if it satisfies it will enter in to is
# otherwise it is skipped

#Syntax for nested if condition

#if(boolean condition):
    #statements                                                # n no of if statement will be allowed 
#elif(boolean condition)
    #statements                                                # n no of elif statement will be allowed
#elif(boolean condition):
    #statements
#else:                                                         #only one else statement will be allowed 
    #statements
