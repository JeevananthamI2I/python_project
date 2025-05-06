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
        
    
list_prblm1()




# def minion_game(string):
    # vowels=('A','E','I','O','u')
    # for i in range(len(string)):
        
    
    # kelvin_count=0
    # stuart_count=0
    # # for i in range(len(string)):
    # kelvin_text=""
    # stuart_text=""
    # for j in range(0,len(string)):
    #     if string[j] in vowels:
    #         kelvin_text+=string[j]
    #         print("if",string[j])
    #         kelvin_count+=1
    #     else:
    #         print(string[j])
    #         stuart_text+=string[j]
    #         stuart_count+=1
    # print(kelvin_text)
    # print(stuart_text)
    # # Stuart
    # for i in range(len(string)):
    #     kelvin_text=''
    #     stuart_text=''
    #     for string[j+1] in range(len(string)):    
    #         if string[j] in vowels:
    #             kelvin_count+=1
    #             kelvin_text+=string[j]
    #             print(string[j]) 
    #         else:
    #             stuart_count+=1
    #             stuart_text+=string[j]
    #             print(string[j])
            
    # print(kelvin_count)     
    # print(stuart_count) 