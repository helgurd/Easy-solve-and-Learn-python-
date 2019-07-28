##Python Higher-Order Functions and Decorators
##In Python, functions are treated as first class objects, allowing you to perform the following operations on functions.  
def sum(a,b):
    total = a + b
    print(total)
    
def sum2(a,b,c):
    c(a,b) # a will become a function and revoke sum() 
    
sum2(3,5, sum) # a and b will passed to c and c passed to sum as function. 
