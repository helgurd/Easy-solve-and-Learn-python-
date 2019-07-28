# Meaning of a single and double underscore before an object name

class Test:
    def __init__(self):
        self.foo=11
        self._bar=23
        self.__baz=42
        
t = Test()
print(dir(t))# we see here the baz is reserved to this class only and attached to the class name hinse not to be interact with other names in other modules or classes
#output 
# \test_ideas\test1.py"
# ['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_bar', 'foo']