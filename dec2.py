def smart(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


@smart
def div(a,b):
    print(a/b)

@smart
def sub(a,b):
    print(a-b)



#@smart
#div=smart(div)
div(2,4)
#sub=smart(sub)
#@smart
sub(1,3)

    
#div(2,4)
#sub(1,3)
