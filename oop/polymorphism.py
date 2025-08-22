class Car:

    def __init__(self,name,model):
        self.name = name
        self.model = model
    
    def move(self):
        print("Driving")

class Boat:

    def __init__(self,name,model):
        self.name = name
        self.model = model
    
    def move(self):
        print("moving the boat")
    
class Plane:

    def __init__(self,name,model):
        self.name = name
        self.model = model

    def move(self):
        print("flying")

c1 = Car("mustang","ford")
b1 = Boat("senorita","chane")
p1 = Plane("airbus","boeing")

for x in (c1,b1,p1):
    x.move()