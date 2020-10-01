class A:
    classvar1="programming lover"
    def __init__(self):
        self.var1="i am a self lover"
        self.classvar1="programming is lover"
class B(A):
    def __init__(self):
        super().__init__()
        print(super().classvar1)
        self.var1="i am inside class B's constructor"
      #  self.classvar1="instance var in class B"
        
    classvar1="i am in class b"
a=A()
b=B()
print(b.classvar1)
