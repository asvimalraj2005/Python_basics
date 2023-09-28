class one:                                                      # we are creating class named one   
    def __init__(self,a,b):                                     # we are initializing the constructor by using __init__ method and passing two parameter a,b
        self.a=a                                                # assigning the values to the variables a,b when passing as an argument while creating objects and instanting them
        self.b=b                                                
    def add(self):                                              # creating a method/function named add and passinf self as an parameter
        print("The sum is ",self.a+self.b)                      # printing the sum of the two varaibles by using self 
    def sub(self):
        print("The difference is",self.a-self.b)

class two(one):                                                 # Inheriting the methods and class members of class one 
    def __init__(self,a,b):                                     # initializing the constructor and passing the required parameter for the methods
        super().__init__(a,b)                                   # By using super class we can able to pass the values from the instance of the class two to class one and access the methods
    def mul(self):
        print("The product is ",self.a*self.b)
    def div(self):
        print("The divident is ",self.a/self.b)


Class_one_object=one(5,6)
Class_one_object.add()

Class_two_object=two(67,70)
Class_two_object.add()

    