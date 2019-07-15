#  first of all before we get into Python lists are not arrays, arrays are two separate things and it is a common mistakes that people think that lists are the same arrays.
#in array if we append different data type will return typeerror which that is not case in the list. 
# ARRAY!=LIST
###example 1 python list
import array
#LIST....................................
aList= [1,2,'monkey' ]
print(aList)


#Appending to the LIST.  
bList= [1,2,3,5,6,7,8,'limon' ]
bList.append('Name')
print(bList,end='')


print('')
#extra list, in this exersice the program only print the numbers that can be  devided by 2:
bList= [1,2,3,5,6,7,8 ]
for x in bList:
    if x % 2==0:
        print([x],end='') 
print('  ')
#ARRAY................................... 
num= array.array('i',[1,2,3,4])
num.append(5)
print(num)

#### this code will not work as we add a different data type to the arry which it is string monkey. 
# num= array.array('i',[1,2,3,4])
# num.append('monkey')
# print(num)