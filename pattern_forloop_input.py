
# Write a Python program to construct the following pattern, using a nested loop number.
#the program should have ueser input.

n = int(input("Enter Number "))
for num in range(n):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")