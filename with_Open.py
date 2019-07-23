
#in with statement you open afile and close automaticly, it dose 2 things in behind the curtain with statemnt call tow methods __enter__() and __exit__
# 
#1 
with open( 'quotes.txt') as f:
    for line in f:
        print(line)

