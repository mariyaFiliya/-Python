def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        print(res)
        yield res


n = int(input("Print number: "))
for i in fact(n):
    print(fact(n))