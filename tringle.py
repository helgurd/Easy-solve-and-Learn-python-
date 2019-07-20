



## Simple  Python Program to check Triangle is Valid or Not

# a = int(input('Please Enter the First Angle of a Triangle: '))
# b = int(input('Please Enter the Second Angle of a Triangle: '))
# c = int(input('Please Enter the Third Angle of a Triangle: '))

# # checking Triangle is Valid or Not
# total = a + b + c
# if total ==180:
#     print("\nThis is a Valid Triangle")

# else:
#     print("\nThis is an Invalid Triangle")

##.....................................................
## Another way to write the solusion for Tringle .        
       
# a = int(input('please input your first side 1\n'))
# b = int(input('please input your first side 2\n'))
# c = int(input('please input your first side 3\n'))
# def tringl_test(leng1,leng2,leng3):
#     if (leng1 > leng2 and leng3) or (leng2> leng1 and leng3) or (leng3 > leng1 and leng2):
#         print('NOP!  you do not have tringle')
#     else:
#         print('Yahoo you made it, you have tringle of  ', leng1+leng2+leng3)
        
        
# tringl_test(a,b,c)


# def check_Triangle(leng):
#     for x in leng:
#         def_leng= (sum(leng)-x)
#         if x> def_leng:
#             return 'NOP this is not triangle '
#         elif x == def_leng:
#             return 'Yes ! you have triangle'
        
#     else:
#         return 'you created '
    
# leng=[]
# for i in range(3):
#     leng.append(int(input('please input your numbers ')))

# print (check_Triangle(leng))



def check_valid_triangle(sides):
    for side in sides:
        other_sides = (sum(sides)-side)
        if side > other_sides:
            return 'No'
        
        
    else:
        side == other_sides
    
   
        
       
sides = []
for i in range(3):
    sides.append(int(input('Enter a side:\n')))

print (check_valid_triangle(sides))