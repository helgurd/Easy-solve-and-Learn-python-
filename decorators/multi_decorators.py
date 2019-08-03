



def upper_conv(func):
    def nested():
        anyf = func()
        return anyf.upper()
    return nested


def split_str(spli):
    def nested():
        spl=spli()
        return spl.split()
    return nested


@split_str
@upper_conv
def mystring():
    return ' hello world what is the point'



print ( mystring())





