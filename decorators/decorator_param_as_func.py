
def div_decorator(fun):
    def inner(*any):
        list1= []
        list1 = any[1:]
        for i in list1:
            if i ==0:
                return 'give normal input'
        return fun(*any)
    return inner
    

@div_decorator
def div1(a,b):
    return a/b

@div_decorator
def div2(a,b,c):
    return a/b/c


print(div2(3,6,5))
print(div1(10,0))