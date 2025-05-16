def dict_ex1():
    a = {'name': "jeeva", 'age': 25, 'place': "chennai"}
    b = [1, 2, 3]

    print({key: {k: v} for key, (k, v) in zip(b, a.items())})

dict_ex1()

def sort_nested_dict(d):
    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = sort_nested_dict(value)
    return dict(sorted(d.items(), key=lambda item: str(item[1]) if not isinstance(item[1], dict) else str(sort_nested_dict(item[1]))))

nested_dict = {'a': {'key': 3}, 'b': {'key': 1},
               'c': {'key': 2, 'inner': {'z': 3, 'x': 1}}}

sorted_dict = sort_nested_dict(nested_dict)
print(sorted_dict)

def simple_coroutine():
    print("Coroutine started")
    x = yield  
    print(f"Received: {x}")

coro = simple_coroutine()
next(coro)        
coro.send(42)
