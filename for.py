for i in range(10+ 1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(10,0,-1):
    for j in range(i):
        print("*", end=" ")
    print() 


for i in range(6):
    for j in range(7):
        if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


print()

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break