a=[]
for i in range(0,11):
        a.append(i)
print(a)
print(hex(id(a)))
print("---------------------------")
for i in a:
        print(hex(id(i)))
#for finding hex address in memory use hex(id())
print("---------------------------")
b=[9,8,7,6,5,4,3,2,1]
print(hex(id(b)))
for i in b:
        print(hex(id(i)))





        