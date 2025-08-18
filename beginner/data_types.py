"""
numeric type
float = decimal
int = whole number
complex = real & imaginary part
Boolean = True/False
none 
sequence = string tuple list
set(mutable)
frozenset(immutable)
key value pair map
dict
curly brackets 
"""

person = {
    'name':'gopal','age':100
}

from enum import unique


a = 10
b = 10.20
c = 3+4j
name = "Arsalan"
list = [1,2,3]
tuple = (2,3,4)
is_running = True
is_sunny = False
unique_number = set([1,2,3,3,4,4])
unique_number2 = {1,2,2,3,3,5,5}
immutable_set = frozenset([1,2,2,3,3,5,5])

result = None
print(result)
print(list)
print(a,b,c)
print(type(a),type(b),type(c))
print(unique_number)
print(unique_number2)
print(immutable_set)