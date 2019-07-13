# Create a program  asks the user to enter their name and their age.
# Any input by user will be stored in the input function and will passed to the created variable, name and age.
# years will calculate the date given  and will subtrac the Data of Birth that given and evaluate the result.
# program has to only accept int if user input str, has to ask user to input the right data types in the field, has to reapet until is true.


name = str(input("please input your name"))
while True:

    try:
        age = int(input("Please enter your age: "))
        years = 2019-age
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
    else:
        print('your age is:', years, '\nyour name is:', name)
        break

print('Thank you ') 


# some tests done here please.
# while True:
#     try:
#         name = str(input('please input your name '))
#         age = int(input('Please input your DOB'))
#     except ValueError:
#         print ('Thank you', age, ' is digit')

#     else:
#         print('your name is:' + name, 'and ', 'your age is:', 2019- age)
#     break
# print ('all done, bye')
# except Exception:

# finally:
#     print('you have to put close()here if open the file')
# Print out a message addressed to thddem that tells them the year that they will turn 100 years old.
