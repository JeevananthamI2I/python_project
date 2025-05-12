import math
import os
import random
import re
import sys

def set_mutations():
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())

    for _ in range(N):
        command_list = list(map(str, input().split()))
        if command_list[0].lower() == 'pop':
            s.pop()
        elif command_list[0].lower() == 'discard':
            s.discard(int(command_list[1]))
        elif command_list[0].lower() == 'remove':
            try:
                s.remove(int(command_list[1]))
            except None:
                pass
    print(sum(s))
    
def add_set():
    N = int(input())
    s = {input() for _ in range (N)}
    print(len(s))
    
def subset_example():
    for _ in range(0, int(input())):
        len_A = int(input())
        A = set(map(int,(input().split())))
        len_B = int(input())
        B = set( map(int, input().split()))
        print(A.issubset(B))

def check_strict_superset():
    a = set(map(int, (input().split())))
    t = int(input())

    b = set(map(int, (input().split())))
    c = set(map(int, (input().split())))

    set_b = a.issuperset(b) and a!=b
    set_c = a.issuperset(c) and a!=c

    if set_b and set_c:
        print(True)
    else:
        print(False)
    
def py_sort_ex():
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())
    
    arr.sort(key=lambda x: x[k])
    for row in arr:
        print(" ".join(map(str, row)))
        
def any_or_all_ex():
    N = int(input())
    arr = list(map(int,input().split()))
    print(all(i>0 for i in arr) and any(str(i)[::-1]==str(i) for i in arr))
    
    
line = input()
def sort_func(char = ''):
  if char.islower(): return -3
  if char.isupper(): return -2
  if char.isnumeric():
    if float(char) % 2 == 1: return -1
    return 0

sorted_line = ''.join(sorted(sorted(line), key=sort_func,))
# print(sorted_line)
    
def set_prblm_ex():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_a = set(map(int, input().split()))
    arr_b = set(map(int, input().split()))

    print(sum(1 if e in arr_a else -1 if e in arr_b else 0 for e in arr))
# any_or_all_ex()
# mark_avrg()
# py_sort_ex()

        
# check_strict_superset()
# add_set()
# set_mutations()
# subset_example()