##forels

# nums= [2,3,4,5, 25]
# for num in nums:
#     if num %6 ==0:
#         print (num)
#         break
# else:
#     print("not found!")
    
  
##Iterable and Itrator  
##Class Itrations 
# class MyRange:
#     def __init__(self, start, end):
#        self.value=start
#        self.end= end
       
#     def __iter__(self):
#         return self
    
    
#     def __next__(self):
#         if self.value >= self.end:
#             raise StopIteration
#         current = self.value
#         self.value +=1
#         return current
    
# nums = MyRange(-5,3)
# for num in nums:
#     print(num)


## Itrating with Generator


def my_iter(start,end):
    current = start
    while current < end:
        yield current
        current +=1 
        
nums = my_iter(1, 10)
for num in nums:
    print(num)



        