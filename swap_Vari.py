# swapping  the value of the varibles value  been made very easer with python 


a= 34
b=45

a,b= b,a


print (a,b)
 
# the out should give after swapping  for a:45 and for b:34 



a = [20,20,10, 10 ]

dup_item=set()
uni=[]
for x in a:
    if x not in dup_item:
        uni.append(x)
        dup_item.add(x)
        
print(dup_item)
print (uni)
