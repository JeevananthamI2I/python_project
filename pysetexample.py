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
    

        
check_strict_superset()
add_set()
set_mutations()
subset_example()