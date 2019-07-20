s = input("Input a string")
d=0
l=0
for c in s:
    if c.isdigit(): #check whether the character is Digit or not. If true, digits value will be incremented
        d=d+1
    elif c.isalpha():#check whether the character is alphabet f true, alphabets value will be incremented
        l=l+1
    else:        # if not digit and alpa pass and not returning anything 
        pass  
print("Letters", l)
print("Digits", d)
