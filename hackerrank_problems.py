
def condition_act(n):
    if n%2==1:
        print("Weird")
    elif n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    elif n%2==0 and  n>=6 and n<=20:
        print("Weird")
    elif n>20:
        print("Not Weird")
        
condition_act(3)

def arithmatic_opration():
    a = 2
    b = 5
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a/b)
arithmatic_opration()

def square_of_range():
    n=6
    list1=[i*i for i in range(n) if n>0]
    for i in list1:
        print(i)
square_of_range()
    
def string_number():   
    # print(''.join(str(i) for i in range(1, n+1)))
    n=5
    sample =""
    for i in range(1,n+1):
        sample +=str(i)
    print(sample)
    
string_number()
    
def list_comprehension():
    x=1
    y=1
    z=2
    n=3
    temp=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
    print(temp)
list_comprehension()
    
def find_runner_up_score():
    n = 5
    list1 = [2, 3 ,6, 6, 5]
    max_n= max(list1)
    filter=[i for i in list1 if i!=max_n]
    run_up=max(filter)
    print(run_up)
find_runner_up_score()   
    
def count_substring(string, sub_string,count=0):
    for i in range(len(string)):
        if string.find(sub_string,i,i+len(sub_string))!=-1:
            count+=1
    return count

count_substring("ABCDCDC","CDC")

def string_validators():
    str_list = "qA2"
    methods = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    q='q'.__getattribute__("isalnum")
    print('q',bool(q))
    for method in methods:
        if any(getattr(char, method)() for char in str_list):
            print(True)
        else:
            print(False)
string_validators()


def marks():
    n = 3
    student_marks={"Krishna":[67, 68, 69],"Arjun":[70, 98, 63],"Malika":[52 ,56 ,60]}
    st_marks = student_marks.get("Malika","key invalid")
    avg_mark=0
    count =0
    for i in st_marks:
         avg_mark +=i   
         count +=1
    re = format((avg_mark/count),".2f")
    print (re)
    
marks()

def tuples_hash():
    # integer_list = map(int, input().split())
    integer_list=[1,2,3,4]
    value_tuple=tuple(integer_list)
    print(hash(value_tuple))
    
tuples_hash()

def list_prblm1():
    N = int(input())
    
    
    list1=[]
    for _ in range(N):
        command = input().split()
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            list1.insert(i,e)
        elif command[0] == "print":
            print(list1)
        elif command[0] == "remove":
            e = command[1]
            list1.remove(e)
        elif command[0] == "append":
            e =command[1]
            list1.append(e)
        elif command[0] =="sort":
            list1.sort()
        elif command[0] =="pop":
            list1.pop()
        elif command[0] =="reverse":
            list1.reverse()
        
    
# list_prblm1()

def nested_list_p1():
    names=[]
    scores=[]
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        names.append(name)
        student.append([name,score])
    value= list(set(scores))
    min_v1=min(value)
    list2=[i for i in scores if i!=min_v1]
    print(student)
    
    # for i in student:
    #     if i[1] == min(list2):
    #         print(i[0])
    print('\n'.join(sorted(i[0] for i in student if i[1] == min(list2))))

    
nested_list_p1()


    
    