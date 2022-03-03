def asterickRightTriangle(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end=' ')
        print("\r")
    print()
asterickRightTriangle(10)

print("Reverse Triangle")
print()

def asterickInvertedTriangle(n):
    for i in range(n, 0, -1):
        for j in range(i+1, 1, -1):
            print('*', end=' ')
        print("\r")
    print()
asterickInvertedTriangle(10)

def asterickRightTriangle(n):
    k = 2 * n - 2
    for i in range(0,n):
        for j in range(0, k):
            print(end=' ')
        k = k - 2
        for j in range(0, i + 1):
            print('*', end=" ")
        print("")
#
asterickRightTriangle(10)