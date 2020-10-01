class myclass:
    x=5
p1=myclass()
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def beauty(self):
        return f"my name is {self.name} and my age is {self.age}"
p1=person("neha",34)
print(p1.name)
print(p1.age)
print(p1.beauty())


class Perso:
    def __init__(mysillyobject,name,age):
        mysillyobject.name=name
        mysillyobject.age=age
    def myfunc(abc):
        print("hello my name is " + abc.name)
p1=Perso("nehaa",23)
print(p1.name)
p1.myfunc()
p1.age=80
print(p1.age)
del p1.age
print(p1.age)
        
