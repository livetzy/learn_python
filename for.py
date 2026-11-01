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

for i in range(10):
    for j in range(i):
        print(' ', end=' ')
    print()
    for k in range(10, i, -1):
        print('*', end=' ')
    print()

for i in range(10):
    for j in range(10, i , -1):
        print(' ', end=' ')
    print()
    for k in range(i):
        print('*', end=' ')
    print()

print("\n=== MOBIL DI BAWAH LANGIT BERBINTANG ===")
for i in range(4):
    for j in range(60):
        if (i * 17 + j * 11) % 43 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(10):
    for j in range(60):
        left_wheel = (j - 18) ** 2 + (i - 7) ** 2
        right_wheel = (j - 43) ** 2 + (i - 7) ** 2
        wheel = 4 < left_wheel <= 10 or 4 < right_wheel <= 10
        inside_wheel = left_wheel <= 4 or right_wheel <= 4
        car_body = (
            (i == 0 and 25 <= j <= 34)
            or (1 <= i <= 2 and (j == 25 - 3 * i or j == 34 + 3 * i or j == 29))
            or (i == 3 and (16 <= j <= 43))
            or (i == 4 and 12 <= j <= 47)
            or (i == 5 and 9 <= j <= 50)
            or (i == 6 and 7 <= j <= 52)
            or (i == 7 and 9 <= j <= 50)
        )
        if wheel or (car_body and not inside_wheel):
            print("*", end="")
        else:
            print(" ", end="")
    print()