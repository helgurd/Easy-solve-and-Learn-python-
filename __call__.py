## what is the __call__ function? 
## The call function as simpl as that we need it when ever we call class object as function.count

class A:
    def __call__(self):
        return('This class called as a function')
        


a = A()

print (a())

    
    


##Try this code to get understand what ment by class object without __call__

# class A:
#     def without(self):
#         return('This class called as a function')
#
#
#
# a = A()

# print (a())

'''result : 
 print (a())
TypeError: 'A' object is not callable
'''
