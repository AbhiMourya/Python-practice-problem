def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


a = 56
b = 96
if (gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('GCD not found')