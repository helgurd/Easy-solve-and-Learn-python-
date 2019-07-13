#write a program in python  to read from file and used more than method. 



# read from file --------------------------------------------------------------------
#write a program in python  to read from file and used more than method. 
# method1
# f=open('str_print.txt','r')
# f.close()
#---------
# method2 called context manager where we use (With and as) and  in this method we don't need to write close() method. 

with open('str_print.txt', 'r') as f:
    f_contents = f.read()
    print (f_contents)

#print in format -------------------------------------------------------
# Write a Python program to print the following string in a specific format (see the output). Go to the editor
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" 
# Output :
# Twinkle, twinkle, little star,
#     How I wonder what you are! 
#         Up above the world so high,
#         Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
#     How I wonder what you are.add()

f='Twinkle, twinkle,\n little star,\n How I wonder what you are!\n Up above the world so high,\n Like a diamond in the sky.\n Twinkle, twinkle, little star,\n How I wonder what you are' 
print (f)


