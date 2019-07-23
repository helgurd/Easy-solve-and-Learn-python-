##forels

# nums= [2,3,4,5, 25]
# for num in nums:
#     if num %6 ==0:
#         print (num)
#         break
# else:
#     print("not found!")
    
  
##Iterable and Itrator  
##Class Itrations 
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


## Itrating with Generator


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

