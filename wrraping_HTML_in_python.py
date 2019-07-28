# This code can be used for all other tags 
# wrraping H1 in the python code: 
def htmlTag(headline):
    def wrapper(msg):
        return ('<' + headline + '>' + msg +'</' + headline +'>')
    return wrapper


h1_tages= htmlTag('h1')
print ( h1_tages('Today\'s  News'))
