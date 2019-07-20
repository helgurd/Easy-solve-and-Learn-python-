# Write a Python program that accepts a string and calculate the number of digits and letters




# s = input("Input a string")
# d=0
# l=0
# for c in s:
#     if c.isdigit(): #check whether the character is Digit or not. If true, digits value will be incremented
#         d=d+1
#     elif c.isalpha():#check whether the character is alphabet f true, alphabets value will be incremented
#         l=l+1
#     else:        # if not digit and alpa pass and not returning anything = letters =0 and Dgits=0
#         pass  
# print("Letters", l)
# print("Digits", d)


##........................................................................
## with special cariactors

# string = input("Please Enter your Own String : ")
# alphabets = digits = special = 0

# for i in range(len(string)):
#     if(string[i].isalpha()):
#         alphabets = alphabets + 1
#     elif(string[i].isdigit()):
#         digits = digits + 1
#     else:
#         special = special + 1
        
# print("\nTotal Number of Alphabets in this String :  ", alphabets)
# print("Total Number of Digits in this String :  ", digits)
# print("Total Number of Special Characters in this String :  ", special)

def countStrings(string):
    alphabets = digits= special =0
    for i in range(len(string)):
        if (string[i].isalpha()):
            alphabets= alphabets +1
        elif(string[i].isdigit()):
            digits=digits +1
        else:
            special = special + 1
print (countStrings(Helloworld 3333*))
        