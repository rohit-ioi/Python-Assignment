

class Student:
    def __init__(self, enrollment_id, subject, hobby):
        self.enrollment_id = enrollment_id
        self.subject = subject
        self.hobby = hobby

pers = Student(123, "Python", "Cricket")
pers2 = Student(234, "Pandas", "Singing")

print(pers.enrollment_id)
print(pers.subject)
print(pers.hobby)









class Car:

    def __init__(self, brand, color, make):
        self.brand = brand
        self.color = color
        self.make = make
    def accelerate(self):
        print(self.brand + "car is accelerating")   

pers = Car("Audi", "Black", 2018)
pers2 = Student("Toyota", "White", 2017)

pers.accelerate()
pers2.accelerate()

print(pers.enrollment_id)
print(pers.subject)
print(pers.hobby)



#  ENCAPSULATION
# we have objects and we don't change their state

class Rectangle:
    def __init__(self, length , width):
        self.__length = length
        self.__width = width

    def getLength(self):
        return self.__length    
    def setLength(self, length):
        self.__length = length
    def getWidth(self):
        return self.__width
    def setWidth(self, width):
        self.__width = width

    def area(self):
        return self.__length*self.__width

    def perimeter(self):
        return 2*(self.__length + self.__width)    



# INHERITANCE
     
# Single Inheritance

class Parent:
    def eat(self):
        print("All of us eat food")
    pass   
class Child(Parent):
    pass
child = Child()
child.eat






class Animal:
    jungle = "Ranthambor"
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    jungle = "Jamnagar"
    def __init__(self, name, breed):
        Animal.__init__(self, name) # Create parent first
        self.breed = breed


dog = Dog("Tommy", "Bulldog")
dog.eat()

print(dog.name)





class Account:
    def __init__(self, title = None, balance=0):
        self.title= title
        self.balance = balance

class SavingAccounts(Account):
    def __init__(self, title, balance, interestRate=0):
        super().__init__(title, balance) # Create parent first
        self.interestRate = interestRate




class Account:
    def __init__(self, title = None, balance=0):
        self.title= title
        self.balance = balance
    def getBalance(self):
        return self.balance
    def deposit(self,amount):
        self.amount +=amount
    

class SavingAccounts(Account):
    def __init__(self, title, balance, interestRate=0):
        super().__init__(title, balance) # Create parent first
        self.interestRate = interestRate






        

