
def plus(fun):
    def inner(x,y):
        if x >y:
            return ( x+y , ' But your first number was ',  int(x) )
        else:
            return x+y
        return fun(x,y)
    return inner
    
@plus
def add(a,b):
    return a +b

print (add(7,5))
        