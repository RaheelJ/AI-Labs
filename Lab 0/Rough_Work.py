from math import sqrt

def is_even(x):
    """If x is even, returns True; otherwise returns False"""
    if (x%2==0):
        return 'True'
    else:
        return 'False'

print (is_even(2))
print (is_even(3))
print (is_even(2.3))
print (is_even(-1066))
print (is_even(-1077))
print (is_even(-1232.3))
####################################################################################


def decrement(x):
    """Given a number x, returns x - 1 unless that would be less than
    zero, in which case returns 0."""
    x = x-1;
    if (x<0):
        x=0;
    return x

print (decrement(2))
print (decrement(-2))
print (decrement(-1))
print (decrement(1))
print (decrement(1.1))
#####################################################################################


def cube(x):
    """Given a number x, returns its cube (x^3)"""
    return x**3

print (cube(2))
print (cube(-2))
print (cube(-5))
print (cube(8))
print (cube(1.1))
####################################################################################


def is_prime(x):
    """Given a number x, returns True if it is prime; otherwise returns False"""
    if (is_even(x)=='True' and x!=2):
        return 'False'
    else:
        i=range(3, int(sqrt(x))+1, 2)
        for j in i:
            if (x%j==0):
                return 'False'
    return 'True'

print (is_prime(9))
print (is_prime(2341))
print (is_prime(22))
print (is_prime(15))
####################################################################################


def primes_up_to(x):
    """Given a number x, returns an in-order list of all primes up to and including x"""
    a=[]
    for i in range(2, x):
        if (is_prime(i)=='True'):
            a.append(i)
    return a

print (primes_up_to(10))
print (primes_up_to(100))
print (primes_up_to(1000))
print (primes_up_to(10000))
####################################################################################


def fibonacci(n):
    """Given a positive int n, uses recursion to return the nth Fibonacci number."""
    if (n==1):
        return 1
    elif (n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

