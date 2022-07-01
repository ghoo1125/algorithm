import math
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = 18
b = 36
# gcd
print(gcd(a, b))
print(math.gcd(a, b))

# lcm
print(abs(a*b) // gcd(a, b))
print(math.lcm(a, b))