def function1(functioni):
    def wrapper():
        print("hello")
        functioni()
        print("welcome to edureka tutorial")
    return wrapper
@function1
def function2():
    print("pythonist")


#function2=function1(function2)
function2()
    
