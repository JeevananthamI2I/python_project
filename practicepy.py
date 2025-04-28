import dis
#list
list1=[1,2,3,4,5]
list2=[2,3,4,"hi",[12,23,34,54]]
list3=[1,2,3,4,5]
list4=[2,3,4,"hi",[12,23,34,54]]
list5=[[1],[2],[3]]
#index access
print(list1[0] is list3[0])
print(list2[4][0] is list4[4][0])
print("hash",hash(list1[0]))
print("id",id(list1))
print("id",id(list3))
print("id4",id(list2[4]))
print("id4",id(list4[4]))
print("id",id(list1[0]))
print("id",id(list3[0]))
print(list2[0])
print(": default",list2[:])
print(list2[-1][0])
print(list2[-1])
print("list5",list5[0][0])


#slicing
print(list1[1:])
print(list1[:2])
print(list1[2:5])
print(list1[-1:5])
print(list1[::2])

#loop
list1=[1,2,3,4,5]
for i in list1:
    print(i)
for i in list1:
    print(i)
    
def gen_ex():
    print("first")
    yield 1
    print("first")
    yield 2
    print("first")
    yield 3
    return 'done'
# dis.dis(gen_ex)
gen1 = gen_ex()
# for i in gen1:
#     print(i)
# for i in gen1:
#     print(i)
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
