#in this program we learn about range in python, range() function will generate the given integer form start to the end for ex:0-10 will generate 0,1,2,3,4,5,6,7,8,9.
import random

# range_num= input('pleaes input any number')
# for num in range (int(range_num)):
#     print (num, end=' ')
    
# above program will print out from 0 to what ever number given.  

#imbeding random.range inside for statement.count
# ran=int(input('input first num'))
# for num in range(random.randrange(ran )):
#     print (num)
    
    
# Extra exercise:  inserting the output number in the list.  

range_num= int(input('pleaes input any number'))
for num in range (range_num):
    n =[num]
    print (n, end=' ')
    