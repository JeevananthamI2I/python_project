
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
    for i in range(n):
        print(i*i)
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
    count= avg_mark= 0
    for i in st_marks:
         avg_mark +=i   
         count +=1
    re = format((sum(st_marks)/len(st_marks)),".2f")
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

    
# nested_list_p1()

def swap_case():
    str1="Jeeva"
    # str2=str1.swapcase()
    str2 =""
    for i in str1:
        if 'A'<= i <='Z':
            str2 +=chr(ord(i)+32)
        elif 'a' <= i <='z':
            str2 +=chr(ord(i)-32)
        else:
            str2 +=i
    print(str2)
swap_case()

def split_str():
    line='hi world'
    # line1=line.replace(" ",'-')
    str1=''.join( '-' if ord(i)==32 else i for i in line)
    print(str1)
split_str()

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first} {last}! You just delved into python.')
print_full_name("jee","va")
def mutate_string(string, position, character):
    print(list(string))
    list1= list(string)
    list1[position]=character
    print (''.join(list1))

mutate_string('jeeva',0,'A')

def hr_pramid_prblm():
    #Replace all ______ with rjust, ljust or center. 

    thickness = 5 #This must be an odd number
    c = 'H'
    print(c.rjust(4)+c+c)

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    # Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    # #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
hr_pramid_prblm()

str1="adfghjjjjjksd"
import textwrap

def wrap(string, max_width):
    inilen = 0

    for i in range(len(string)):

        print(string[i],end ='')
        inilen+=1
        if inilen == max_width:
            inilen = 0
            print('\n',end='')

    return ''

def designer_door_mat():
    n, m = map(int, input().split())
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n-2, 0, -2):
        print((".|." * i).center(m, "-"))
        
import string
def print_rangoli(size):
    a=list(string.ascii_lowercase)[:size]
    temp=a[::-1]
    n=(size-1)*4 +1
    for i in range(1,size+1):
        print('-'.join(temp[:i]+((temp[:i])[::-1])[1:]).center(n,'-'))
    for i in range(size-1,0,-1):
        print('-'.join(temp[:i]+((temp[:i])[::-1])[1:]).center(n,'-'))

