# ''' # real world objects have some attributes, and then certain behaviour 
# # procedural programming is the programming which are written and executed in the form of procedures(steps) and works on yes/no in every step
# # then object oriented programming was invented on the concepts of objects
# # objects( state - attributes , behaviour - methods/functions)

# # Relationship ----  Programming  ----   OOPS concept

# # class is a keyword and Person is the name of the class
# # class name should have its first letter in capital letter
# class Person : 
#     pass  
# # this is the simplest initialization of a class

# per_obj = Person()
# print(per_obj)


# class Guy :
#     # logic to create Guy object with attributrs
#     # Initializer or constructor function
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# per = Person("Vishwa", 99)
# print(per.name)
# print(per.age) 

# per1 = Person("Ambani", 89)
# print(per1.name)
# print(per1.age)




# class Student:
#     def __init__(self, enrollment_id, subject, hobby):
#         self.enrollment_id = enrollment_id
#         self.subject = subject
#         self.hobby = hobby

# pers = Student(123, "Python", "Cricket")
# pers2 = Student(234, "Pandas", "Singing")

# print(pers.enrollment_id)
# print(pers.subject)
# print(pers.hobby)


# # self is used to denote the objects
# # if we initialise multiple init in OOPs then Python class only consider last init and every other init will be ignored
# # only one init should be initialized


# class Helloperson :
#     def __init__(self, name, age = 99, hobby = "Cricket"):
#         self.name = name
#         self.age = age
#         self.hobby = hobby

# per1 = Helloperson("Vishwa") 
# per2 = Helloperson("Mohan", 53)
# per3 = Helloperson(name = "Vishwa Mohan", hobby = "Football")



# ''' Properties/State
#    1. Object property
#    2. Class Property
#      '''

# class Person:
#     country = "India"
#     def __init__(self, name, age):
#         self.name = name
#         self.age  = age

# per1 = Person("Vishwa", 99)
# per2 = Person("Mohan", 98)

# print(per1.name, per1.country)
# print(per2.name, per2.country)





# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dance(self):
#         print("I can also dance!!!")


# per = Person("Vishwa", 99)
# per.dance()





# class Person: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def dance(self):  # this is a method
#         print(self.name + "I can also dance!!!")


# per = Person("Vishwa", 99)
# per.dance()





# '''


class Point:



    def __init__(self, x,y,z):     
        self.x = x
        self.y = y
        self.z = z


    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2   
    

    
obj = Point(1,2,3)
print(obj.sqSum())    
''' x,y,z are the objects/ instance variable'''                  


# methods  ----   1. instance method   ----  the above methosd was instance method
#                  2. Class method   -----  
#                 3. static method




# static method

class  Person : 
    counrty = "India"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def gaming(cls):
        print("I live in the country : ", cls.country)
        print("Humko bas khelne me maja aata hai!")

            
# every object will have the class method

Person.gaming()
per = Person("Vishwa", 99)




class Cricket :
    def __init__(self, player1, player2, fight):
        self.player1 = player1
        self.player2 = player2
        self.__fight = fight


    def __internal_coversation():
        print("Dhoni you just missed a stump today!")

    def play(self):
        print("I am copy cricket champion")

cric = Cricket("MS Dhoni", "Virat Kohli", "Say some fight happened")

print(cric.player1)
cric.play()
# we can initialise private modifiers but will not print but will work if we initialise inside def function







