class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=f"this email is {self.fname} {self.lname}"
    def explain(self):
        return f"this email is {self.fname} {self.lname}"
t1=Employee("Hindustanni","supporter")
print(t1.email)
#t1.email="neha@gmail.com"
t1.fname="neha"
print(t1.email)
        
