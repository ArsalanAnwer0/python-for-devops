a = 100
b = 30
c = 50
    
env = "dev"

if env == "dev":
    print("Load dev application")
else:
    print("Not in dev environment")
    
def check_biggest(a,b,c):
    if a > b and a > c: # if this line is true then only the control flows goes inside
        print("A is bigger")
        print("Yes, I want to tell again that A is bigger")
    elif b > a and b > c:
        print("B is bigger")
    elif c > a and c > b:
        print("C is bigger than everyone")
    else: # if two or more numbers are equal
        print("Two or more numbers are equal")
        
check_biggest(2,3,6)