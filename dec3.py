def func1(name):
    return f"Hello {name}"


def func2(name):
    return f"{name} , how you doing"

def func3(func4):
    return func4('Dear learner')

print(func3(func1))
print(func3(func2))
