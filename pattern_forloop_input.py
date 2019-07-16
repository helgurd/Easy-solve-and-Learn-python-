


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



# Write a Python program to construct the following pattern, using a nested loop number.
#the program should have ueser input.

n = int(input("Enter Number "))
for num in range(n):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")