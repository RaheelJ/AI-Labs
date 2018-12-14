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
    if (is_even(x)=='TRUE'):
        return 'False'
    else:
        for i in rang(3, 2, abs(x/2)):
            if (x%i=='True'):
                return 'False'

