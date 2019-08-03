
# ## first step only to learn how decorators will start, however, this is not the way we call decorator - 
# ##rather we use the style with @ symbol  

# def decoUperchanger(me): # main function will take one parameter
#     def inner(): # nested function created 
#         str1=me() # the parameter  assigned to name and handeld as function. 
#         return str1.upper() # built in function implemented on the nested function  
#     return inner # main function will return the nested function. 
   
   
# # the function would like not to be touched and only applying other function on it .      
# def messagee():
#     return ' hello world' # text will turn to upper case 

# a = decoUperchanger(messagee) # we assigne to a name 

# print (a()) # the name in decorator has to take parenthesis

### Step2 with @ symbol: the correct way to work 

def decoUperchanger(me): # main function will take one parameter
    def inner(): # nested function created 
        str1=me() # the parameter  assigned to name and handeld as function. 
        return str1.upper() # built in function implemented on the nested function  
    return inner # main function will return the nested function. 
   
   

@decoUperchanger    ###we sill add this line of code on top of any function  
def messagee():
    return ' hello world' # text will turn to upper case 

###a = decoUperchanger(messagee) # this is not needed  

##print (a()) # this is not needed 


print (messagee())