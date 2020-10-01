class A:
    classvar1="programming lover"
    def __init__(self):
        self.var1="i am a self lover"
        self.classvar1="programming is lover"
class B(A):
    classvar1="i am in class b"
a=A()
b=B()
print(b.classvar1)
