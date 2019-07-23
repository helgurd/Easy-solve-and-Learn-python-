class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name= last_name
        self.eye = eye_color




class Child(Parent):
    
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.toys= number_of_toys

billy= Parent('helgurd', 'Blue')
child=Child('Rez', 'Red', 5)
print (billy.last_name, billy.eye)
print( child.last_name,  child.toys)
