##Python Higher-Order Functions and Decorators
##In Python, functions are treated as first class objects, allowing you to perform the following operations on functions.  
# def sum(a,b):
#     total = a + b
#     print(total)
    
# def sum2(a,b,c):
#     c(a,b) # a will become a function and revoke sum() 
    
# sum2(3,5, sum) # a and b will passed to c and c passed to sum as function. 

###..........................assigning function to variables 
# def sum(a,b):
#     total= a+b
#     return( total)
    
# d= sum ## we can add parnthes or without it, for ec, a=sum(4,5),or we can go just as follow 
# print(d(3,6))


### Clousers: 


# def outer_func(msg):
#     message = msg
    
#     def inner_func():
#         return( message)
        
#     return inner_func

# myfunc=outer_func('hi')   
# myfunc1=outer_func('hello')   
# print (myfunc1())
# print (myfunc())


# wrraping H1 in the python code: 
def htmlTag(tag):
    def wrapp(msg):
        return ('<' + tag + '>' + msg +'</' + tag +'>')
    return wrapp
h1_tages= htmlTag('h1')
print ( h1_tages('Head line 1'))

