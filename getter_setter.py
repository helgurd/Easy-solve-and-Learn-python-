
##Getter and Setter in Python
##We use getters & setters to add validation logic around getting and setting a value.
##To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by the external user.



##
# class Student: 
#     def __init__(self, marks):
#         self.__marks=marks
#     def per(self):
#         return (self.__marks/600 *100)
       
#     def set_value(self,value): #setter useually takes 1 parameter with self
#         self.__marks=value
#     def getter(self): # getter has no parameters except for self 
#         return self.__marks
        
# s = Student(555)
# #s.marks= 599
# s.setter(666)
# print(s.getter())
# print(s.per(), '%')

# #print(s.marks)

#### -------------  
# class Employee:
#     def __init__(self, first, last):
#         self.first =first
#         self.last= last 
#         #self.email = first+'.' +  last +'@gmail.com'
#     @property
#     def email(self):
#         return '{}.{}@gmail.com'.format(self.first, self.last)
        
# def fullname(self):
#     return'{} {}'.format(self.first, self.last)


# emp_1= Employee('Jone','Smith')

# print(emp_1.email)

'''onther Example and tips: when you implamenting  GET  
property   functions you have to call the name 
you already given to the set function see the exmaple  '''


class Myclass:
    def __init__(self):
     self.__number =-1 # __number is the private, any private objects will by highlited with dunder
     
    @property # propererty decorator
    def anyA(self):# get method 
        print('Getting anyA')  
        return self.__number
    @anyA.setter # as can be seen here we adding a getter method name as part of property 
    def anyA(self, value):
        print('setting Value')
        self.__number=value
        
    @anyA.deleter
    def anyA(self):
        print('deletr call')
        del self.__number
        
obj2= Myclass()
print(obj2.anyA)       
obj2.anyA = 3344
print(obj2.anyA)
 