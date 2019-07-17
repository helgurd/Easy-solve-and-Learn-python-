


# # simple constrat of the Pattren
# # Write a Python program to construct the following pattern, using a nested loop number.
# # 1                                                                                                             
# # 22                                                                                                            
# # 333                                                                                                           
# # 4444                                                                                                          
# # 55555                                                                                                         
# # 666666                                                                                                        
# # 7777777                                                                                                       
# # 88888888                                                                                                      
# # 999999999
# for i in range(10):
#     print(str(i) * i)

##.................................................
#sample2  

# #  Write a Python program to construct the following pattern, using a nested for loop.
# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 


n = int(input("Enter Number "))
#n=10  ##you can uncomment this line and comment the input by user to get a fixed pattern. 
print('you printed', n, 'stars')
for i in range(n):
    for j in range(i):
        print ('*', end="") # you can remove * and input anythin you would like to be printed, for numbers you have to replace the * with (n) without quats just like this (n, end="")  
    print('\n')







# # # Write a Python program to construct the following pattern, using a nested loop number.
# # #the program should have ueser input.

