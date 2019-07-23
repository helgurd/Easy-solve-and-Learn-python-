#  a class which will count the number    
class Apples:
      
    ApllesInTheBasscet= 0
    
    def __init__(self, apples):
        self.apples= apples
        Apples.ApllesInTheBasscet += 1
     
        
app1= Apples(1)
app2=  Apples(2)
app3= Apples(3)
app4= Apples(4)



print('Number of the Apples  in the Basscet are:', str(Apples.ApllesInTheBasscet))

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
