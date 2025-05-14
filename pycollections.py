from collections import defaultdict
from collections import namedtuple
from collections import OrderedDict
from collections import Counter
from collections import deque
from itertools import chain
from itertools import groupby




def default_dict_example():
    n, m = map(int, input().split())
    group_a = [input().strip() for _ in range(n)]
    group_b = [input().strip() for _ in range(m)]
    index_map = defaultdict(list)
    for idx, word in enumerate(group_a, start=1):
        index_map[word].append(idx)

    for word in group_b:
        if word in index_map:
            print(" ".join(map(str, index_map[word])))
        else:
            print(-1)

            
def named_tuple_example():
    N =int(input())
    student = namedtuple("Student", input().split())
    stu_mark=0
    for _ in range(N):
        s = student (*input().split())
        stu_mark+=int(s.MARKS)
        
    print (stu_mark/N)
    
def ordered_dict_example():
    net_price = OrderedDict()
    for _ in range( int(input()) ):
        name, price = input().rsplit(' ',1)
        net_price[name] = int(price) + net_price[name] if name in net_price else int(price)

    for k,v in net_price.items():
        print(k, v)
        
def counter_example():
    n=int(input())
    l=[input() for _ in range(n)]
    print(len(Counter(l)))
    for i in Counter(l).values():
        print(i,end=' ')

def deque_example():
    q = deque()
    for _ in range( int(input()) ):
        operation, *value = input().split()
        # print(operation, value)
        method = getattr(q, operation)
        method(*value)
    print(*q)
    
def pillingUp_example():
    n = int(input())
    for _ in range(n):
        num = int(input())
        blocks = list(map(int, input().split()))
        print(blocks)
        middleIndex = blocks.index(min(blocks))
        left = blocks[:middleIndex]
        right = blocks[middleIndex:]
        if left == sorted(left,reverse = True) and right == sorted(right):
            print("Yes")
        else:
            print("No")
            
def most_commons_ex():
    s = Counter(sorted(input())).most_common(2)
    for i in s:
        print(*i)
        
def set_intersection_ex():
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    print(len(s1.intersection(s2)))
    
def set_difference_ex():
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    print(len(s1.intersection(s2)))
    
def set_or_example():
    s1 = set(map(int, input().split()))
    s2 = set(map(int, input().split()))
    print(len(s1|(s2)))
    
def captain_room():
    from collections import Counter

    K = int(input())
    room_numbers = list(map(int, input().split()))
    counter = Counter(room_numbers)

    for room, count in counter.items():
        if count == 1:
            print(room)
            break

def python_quest_1(): 
    n=int(input())
    # # print(i: for i in range(int(input())))
    for i in range(1,n+1):
        print(i**-1)
        # print(10**i-1)
        print("iiii",i)
        print((10**i-1)//9)
        # print(i*((10**i-1)//9))
python_quest_1()

def collection_ex1():
    nested_dict = {'A': {'score': 85, 'age': 25},
               'B': {'score': 92, 'age': 30},
               'C': {'score': 78, 'age': 27}}
    print(dict(sorted(nested_dict.items(), key=lambda x: (x[1]['score']))))
    
def dict_ex1():
    sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 1}

    # Sorting using a for loop
    sorted_dict = {key: sample_dict[key] for key in sorted(sample_dict, key=sample_dict.get)}
    print(sorted_dict)

def dict_ex2():
    nested_dict = {'a': {'key': 3}, 'b': {'key': 1}, 'c': {'key': 2}}
    sorted_dict = dict(sorted(nested_dict.items(), key=lambda item: item[1]['key']))
    print(sorted_dict)
    
def iter_tool_ex():
    d = {"a": [1, 2], "b": [3, 4], "c": [5]}
    res = list(chain(*d.values()))

    print(res)
    
def dict_ex_3():
    d = namedtuple("d", "Name")
    li = [d("jeeva"), d("lokesh"), d("vasanth")]
    li.sort(key=lambda x: x.Name)
    grouped = groupby(li, key=lambda x: x.Name)
    for key, group in grouped:
        for item in group:
            print({'Name': item.Name})
dict_ex2()
iter_tool_ex()
# set_difference_ex()
# set_intersection_ex()
# set_or_example()
# most_commons_ex()
# pillingUp_example()
# default_dict_example()
# deque_example()
# named_tuple_example()
# ordered_dict_example()
