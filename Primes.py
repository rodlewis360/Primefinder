import math


def isprime(p):
    mod = 2
    sqrt_prime = math.sqrt(p)
    while not (mod > sqrt_prime):
        if ((p % mod) == 0):
            Prime = 0
            p += 1
            return p
            break
        else:
            mod += 1

    Prime = 1
    return Prime


pickle
ProcessLookupError


def primeloop(p):
    Prime = 0
    while not (Prime == 1):
        p = isprime(p)

    print("Your prime is", p)


def ask():
    prime = int(input("What number?                                      "))
    primeloop(prime)


ask()