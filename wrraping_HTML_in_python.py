# This code can be used for all other tags 
# wrraping H1 in the python code: 
def htmlTag(headline):
    def wrapper(msg):
        return ('<' + headline + '>' + msg +'</' + headline +'>')
    return wrapper

h1_tages= htmlTag('h1')
h2_tages= htmlTag('h2')
p_tages= htmlTag('p')
print ( h1_tages('Today\'s  News'))
print ( h2_tages('Today\'s  News'))
print ( p_tages('Today\'s  News'))
