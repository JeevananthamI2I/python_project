def dict_ex1():
    a = {'name': "jeeva", 'age': 25, 'place': "chennai"}
    b = [1, 2, 3]

    print({key: {k: v} for key, (k, v) in zip(b, a.items())})

dict_ex1()
# Input : test_dict = {“a” : {“b” : {}}, “d” : {“e” : {}}, “f” : {“g” : {}} 
# Output : {‘b’: {‘a’: {}}, ‘e’: {‘d’: {}}, ‘g’: {‘f’: {}} Explanation : Nested dictionaries inverted as outer dictionary keys and viz-a-vis. Input : test_dict = {“a” : {“b” : { “c” : {}}}} Output : {‘c’: {‘b’: {‘a’: {}}}} Explanation : Just a single key, mapping inverted till depth.

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
        print("exit")
f = fib()
for _ in range(10):
    print(next(f))