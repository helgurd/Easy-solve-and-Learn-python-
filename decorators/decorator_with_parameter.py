
def main_fun(anyage):
    def deco(fun):
        def inner():
            return fun() + anyage
        return inner 
    return deco


@main_fun('Helgurd')
def morning():
    return ' Good morning '


print (morning())
