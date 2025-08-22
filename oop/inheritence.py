class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    
    def PrintName(self):
        print(self.fname, self.lname)

class student(Person):
    pass

x = student("om","vasava")
x.PrintName()

# p1 = Person("rahul","kumar")
# p1.PrintName()