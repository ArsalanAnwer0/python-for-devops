set1 = {1, 3, 5, 7, 9}
set2 = {2, 4, 5, 6, 9}

print(f"set1: {set1}")
print(f"set2: {set2}")

Union = set1 | set2
print("Union:",Union)
Intersection = set1&set2
print("Intersection",Intersection)
Difference = set1 - set2
print("Difference",Difference)
orig = [1, 1, 2, 2, 3, 3, 4, 5]
new = set(orig)
print("Unique Numbers: ",new)
number = int(input("Enter a number to search: "))
set1 = {1,3,5,7,9}
set2 = {2,4,5,6,9}

in_set1 = number in set1
in_set2 = number in set2

if in_set1 and in_set2:
    print("Number found in both sets!")
elif in_set1:
    print("Number found in set1 only")
elif in_set2:
    print("Number found in set2 only")
else:
    print("Number not found in either set")




