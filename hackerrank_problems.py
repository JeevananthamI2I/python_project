
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
    str_list = list("qA2")
    methods = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']

    for method in methods:
        if any(getattr(char, method)() for char in str_list):
            print(True)
        else:
            print(False)
string_validators()
    