# forels

# nums= [2,3,4,5, 25]
# for num in nums:
#     if num %6 ==0:
#         print (num)
#         break
# else:
#     print("not found!")


##Iterable and Itrator
# Class Itrations
# class MyRange:
#     def __init__(self, start, end):
#        self.value=start
#        self.end= end

#     def __iter__(self):
#         return self


#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value +=1
#         return current

# nums = MyRange(-5,3)
# for num in nums:
#     print(num)


# Itrating with Generator


# def my_iter(start,end):
#     current = start
#     while current < end:
#         yield current
#         current +=1

# nums = my_iter(1, 10)
# for num in nums:
#     print(num)

# class Base:
#         num=0
#         def __init__(self):
#                 Base.num+=1
#         def getnum():
#                 return(Base.num)
# print(Base.getnum)

# class Apples:

#     ApllesInTheBasscet= 0

#     def __init__(self, apples):
#         self.apples= apples
#         Apples.ApllesInTheBasscet += 1


# app1= Apples(1)
# app2=  Apples(2)
# app3= Apples(3)
# app4= Apples(4)


# print('Number of the Apples  in the Basscet are:', str(Apples.ApllesInTheBasscet))

# class Student:

#     number_of_students= 0

#     def __init__(self, name, grade):
#         self.name= name
#         self.grade= grade
#         Student.number_of_students += 1


# Student1= Student("John Philips", 10)
# Student2= Student("Michelle Matthews", 9)
# Student3= Student("Michael Robers", 11)
# Student4= Student("Yorshew Tomson", 12)
# Student5= Student("Ryan Matts", 12)

# print("The number of students in the class is " + str(Student.number_of_students))


# user directory
# import os
# home = str(os.path.expanduser('~'))
# print(home)

# a = 7
# b= 2
# z = a//b

# print (z)

# test one variable against multiple values

# x=2
# if x in (1,3,4):
#     print ('found')
# else:
#     print('try again')


# import subprocess
# #import os
# # subprocess.call(['ls', '-l'])

# #command = ' cmd'
# # os.system(command)
# from subprocess import call
# call(["dir"])

# class Test:
#     def __init__(self):
#         self.foo=11
#         self._bar=23
#         self.__baz=42

# t = Test()
# print(dir(t))# we see here the baz is reserved to this class only and attached to the class name hinse not to be interact with other names in other modules or classes
# #output
# # \test_ideas\test1.py"
# # ['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']


# while True:
#     userin= input('>>')
#     if len(userin) ==1:
#         break
#     print('you should enter one chareactor')

# for i in range(10):
#     print(i)
# import pdb
# x=20
# y=100
# if x>y:
# pdb.set_trace()
#     print('yesgreater')
# else:
#     print ( 'nop')

# any= 'x greater' if x > y else ' y greater'
# print (any)
# n = float(input())

# print (n)

# print (type(n))

# def hello_name(name: str) -> str:
#     return(f"Hello {name}")

# print(hello_name('helgurd'))

# def add_this(a: int, b: int) -> int:
#     return a+b



# # print(add_this(4, 6))

# # p1 = add_this(5, 6)

# # print(p1.__doc__)

# # print (__doc__)
# # print(help(p1))


#-----------------------------------------------

# import datetime
 
# curr_Month =  datetime.date.today().strftime("%B")
 
 
 
# #Functionas are created for each case
 
# def Jan ():
 
#    print("January - Starting new Year")
 
  
 
# def Feb ():
 
#    print("February - The Second Month")
 
  
 
# def Mar ():
 
#    print("March - The Third Month")
 
  
 
# def Apr ():
 
#    print("April - The Fourth Month")
 
  
 
# def May ():
 
#    print("May - The Fifth Month")
 
  
 
# def Jun ():
 
#    print("June - The Sixth Month")
 
  
 
# def Jul ():
 
#    print("July - The Seventh Month")
 
  
 
# def Aug ():
 
#    print("August - The Eighth Month")
 
  
 
# def Sep ():
 
#    print("September - The Ninth Month")
 
  
 
# def Oct ():
 
#    print("October - The Tenth Month")
 
  
 
# def Nov ():
 
#    print("November - The Eleventh Month")
 
  
 
# def Dec ():
 
#    print("December - The End of Year")
 
 
 
# #Dictionary containing all possible values
 
# Month_Dict = {
 
#     "January": Jan,
 
#     "February": Feb,
 
#     "March": Mar,
 
#     "April": Apr,
 
#     "May": May,
 
#     "June": Jun,
 
#     "July": Jul,
 
#     "August": Aug,
 
#     "September": Sep,
 
#     "October": Oct,
 
#     "November": Nov,
 
#     "December": Dec   
 
#     }
 
 
 
# #The switch alternative
 
# Month_Dict.get(curr_Month)()

# import os 
# home = str(os.path.expanduser('~user'))
# print (home)


# def switch():
#     value1= int(input('ENTER FIRST VALUE'))
#     value2= int(input('ENTER SECOND VALUE'))
#     print( 'press 1 for add \n press 2 for sub \n press 3 for multi \n press 4 for devision')
#     option= int(input('Enter your option'))
#     def add():
#         result= value1 + value2
#         print ( result)
#     def sub():
#         result= value1 - value2
#         print ( result)
#     def mul():
#         result= value1 * value2
#         print ( result)
#     def dev():
#         result= value1 / value2
#         print ( result)
#     dect={
#         1:add,
#         2:sub,
#         3:mul,
#         4:dev }
#     dect.get(option)()

# print (switch())

# b = 2 
# if b in (1,3,2,4,5,6):
#     print ( 'yes ')
# else:
#     print('none')
# import subprocess

# subprocess.call('')


# def myname():
#     print('My name Halgurd')
    
# if __name__ == "__main__":
#     myname()
 
# def main():
#         print('Hello Wolrd')
        



    
# print (' Guru')

import subprocess
out=subprocess.call('ipconfig')
print (out)


