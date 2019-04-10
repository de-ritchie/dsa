# Uses python3
import sys

def gcd_naive(a, b):
    
    mod = a % b
    if mod == 0 :
        return b
    else :
        return gcd_naive(b, mod)

def lcm_naive(a, b):
    gcd = gcd_naive(a, b)
    # print(gcd)
    # print((a*b)//gcd)
    return ((a*b)//gcd)

# print(lcm_naive(226553150, 1023473145))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

