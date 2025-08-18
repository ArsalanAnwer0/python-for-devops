
gen = [1,2,3,4,5,6,7,8,9,10]
print(gen)
even_squares = [x**2 for x in gen if x % 2 == 0]
print(even_squares)
word_list = ["cat","elephant","dog","butterfly","ant"]
long_word = [name for name in word_list if (len(name) > 5)]
print(long_word)
# greater_than_five = [x for x in gen if x > 5]
greater_than_five = list(filter(lambda x: x > 5, gen))
print(greater_than_five)
small_case = ["arsalan"]
res = map(str.upper,small_case)
print(list(res))