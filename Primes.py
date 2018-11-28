import math


def isprime(p):
    mod = 2
    sqrt_prime = math.sqrt(p)
    while not (mod > sqrt_prime):
        nPrime = 0
        if ((p % mod) == 0):
            Prime = 0
            p += 1
            nPrime = 1
            break
        else:
            mod += 1

    Prime = 1
    return (nPrime, p, Prime)


def primeloop(p):
    Prime = 0
    nPrime = 1
    while (nPrime == 1) or not (Prime == 1):
        nPrime = 0
        print("calculating", p)
        q = isprime(p)
        nPrime, p, Prime = q

    print("Your prime is", p)


def ask():
    prime = int(input("What number?                                      "))
    print("calcuating")
    primeloop(prime)


ask()
