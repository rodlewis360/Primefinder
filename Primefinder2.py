def findprime():
    times = 0
    timeswrong = 0
    from time import sleep
    import math
    Prime = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    for i in Prime:
        i = (i**2) - 2
        print(i)
        times, timeswrong, nPrime = isprime(i, times, timeswrong)
        print(nPrime)
        sleep(1)
    print("This algorithm was correct",times - timeswrong,"times out of",times,"times!")

import math


def isprime(p, times, timeswrong):
    mod = 2
    sqrt_prime = math.sqrt(p)
    while not (mod > sqrt_prime):
        nPrime = True
        if ((p % mod) == 0):
            nPrime = False
            timeswrong += 1
            break
        else:
            mod += 1
    times += 1
    return (times, timeswrong, nPrime)


