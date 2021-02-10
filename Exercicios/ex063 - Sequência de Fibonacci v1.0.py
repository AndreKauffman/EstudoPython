print("Fibonacci")
print("===============")
num = int(input("Termo: "))
t1 = 0
t2 = 1
cont = 0
while cont <= num:
    print("{} -> ".format(t1,t2), end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont+=1
print("FIM")


