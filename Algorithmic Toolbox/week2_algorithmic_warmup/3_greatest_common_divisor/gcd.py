# Uses python3
import sys

def gcd_naive(a, b):
    
    mod = a % b
    if mod == 0 :
        return b
    else :
        return gcd_naive(b, mod)

# print(gcd_naive(28851538, 1183019))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
