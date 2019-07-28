#Subprocess moduleSystem Call in 

# import subprocess
# out=subprocess.call('ipconfig')
# print (out)


# import os ## os is come with python.
# current_directory= os.getcwd() # will find the current work place 
# print(current_directory)

#os.mkdir('newfoderHelg')  # creates new folder in the  current work directory cwd. 
#os.rename('newfoderHelg', ' anyName') # will Rename created director 
#os.rmdir('anyName')
# help(os)
##-----------------------
# Decorator 

# def mydecorator(f):
#     def wrapper():
#         print('Inside of the decorator before calling the function.')
#         f()
#         print ('Inside of the docorator after calling the function')
#     return wrapper 


# @mydecorator
# def printName():
#     print('Antoni')
    
# printName
##Python Higher-Order Functions and Decorators
##In Python, functions are treated as first class objects, allowing you to perform the following operations on functions.  
def sum(a,b):
    total = a + b
    print(total)
    
def sum2(a,b,c):
    c(a,b) # a will become a function and revoke sum() 
    
sum2(3,5, sum) # a and b will passed to c and c passed to sum as function. 

    
    
    