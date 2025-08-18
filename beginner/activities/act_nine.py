# Learning *args and **kwargs

def func1(*args):
    print(f"Arguments passed: {args}")
    result = sum(args)
    return result

def func2(**kwargs):
    for i,k in kwargs.items():
        print(f"{i}:{k}")


print(func1(1,2,3))

func2(name="Arsalan",school="SCSU")

# Flexibilty calculator with args and kwargs



def calculate(*args,**kwargs):
    for x in kwargs.values():
        if x == "add":
            result = sum(args)
            return result

print(calculate(5,3,operation="add"))

def create_profile(**kwargs):
    for x,y in kwargs.items():
        if x == "name":
            print("Profile for",y)
    for k,w in kwargs.items():
        print(f"{k}:{w}")


create_profile(name="Arslan",age=25,city="NYC",job="Engineer")