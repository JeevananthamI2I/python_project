import string
from itertools import product
from itertools import permutations
from functools import reduce



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

def split_str():
    line='hi world'
    # line1=line.replace(" ",'-')
    str1=''.join( '-' if ord(i)==32 else i for i in line)
    print(str1)

def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')

def mutate_string(string, position, character):
    print(list(string))
    list1= list(string)
    list1[position]=character
    print (''.join(list1))


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


def wrap(string, max_width):
    count = 0

    for i in range(len(string)):

        print(string[i],end ='')
        count+=1
        if count == max_width:
            count = 0
            print('\n',end='')

    return ''

def designer_door_mat():
    n, m = map(int, input().split())
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range(n-2, 0, -2):
        print((".|." * i).center(m, "-"))
        

def print_rangoli(size):
    a=list(string.ascii_lowercase)[:size]
    temp=a[::-1]
    n=(size-1)*4 +1
    for i in range(1,size+1):
        print('-'.join(temp[:i]+((temp[:i])[::-1])[1:]).center(n,'-'))
    for i in range(size-1,0,-1):
        print('-'.join(temp[:i]+((temp[:i])[::-1])[1:]).center(n,'-'))
        
def solve(text):
    text_result=''
    for i in range(len(text)):
        if i == 0 or text[i-1]==" ":
            text_result+=chr(ord(text[i])-32) if 'a' <= text[i]<='z' else text[i]
        else:
            text_result+=text[i]    
    print(text_result)
    
def matrix_problems():
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in ((i,j) for i in a for j in b):
        print(i,end=" ")
    # print(list(product(a,b)))

def permutation_prblm():
    text=input().split()
    result=sorted(tuple((map(lambda i:"".join(i),permutations(text[0],int(text[1]))))))
    for i in result:
        print(i)
        
def average(array):
    # your code goes here
    # avarage=sum(set(array))/len(set(array))
    print(sum(set(array))/len(set(array)))

def exception_program():
    a=3
    b=1
    
    try:
        print(a//b)
    except (ZeroDivisionError,ValueError) as e:
        print ("Error Code:",e)

exception_program()      
# average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])

# permutation_prblm()
# matrix_problems()    
# minion_game("BANANA")
# solve("hi world")
# swap_case()
# split_str()
# print_full_name("jee","va")
# mutate_string('jeeva',0,'A')
# hr_pramid_prblm()
# wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',5)
# designer_door_mat()
# print_rangoli(5)