# Given a list and a number find two numbers in the list that sums up to the number given


    
a = [1,2,3,4,5,6,7,8,10,11,12,13]
b=14
c=[]
for i,y in enumerate(a): 
    for d in range(i, len(a)):
        tow= a[i] + a[d]
        if tow ==b:
            c.append((a[i], a[d]))
            print(c)