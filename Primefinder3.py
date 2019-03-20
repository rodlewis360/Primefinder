def fib(n):
    a, b = 0, 1
    lst = [0, 1]
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        lst.append(b)
    print()
    return lst

def primefinder():
    print("How high?")
    fibonacci = fib(input())
    for a in fibonacci:
        lst.append(6 * a)
    for a in lst:
        print(a)
        
