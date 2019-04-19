a = 12345
b = 1234


def gcd(x, y):
    x, y = min(x, y), max(x, y)
    while x:
        x, y = y % x, x
    return y

print(gcd(a, b))



def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(a, b))
