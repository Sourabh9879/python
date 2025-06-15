class programmer:
    company = "Microsoft"
    salary = 15000
    
    def __init__(self, name):
       self.name = name
       

s = programmer("sourabh")
print(s.name, s.company, s.salary)

r = programmer("raj")
print(r.name, r.company, r.salary)

