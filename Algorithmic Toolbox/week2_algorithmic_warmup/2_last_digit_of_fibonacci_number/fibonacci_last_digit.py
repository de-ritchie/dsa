# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    
    sum = prev = 0
    for i in range(n):
        if i == 0 or i == 1:
            sum = 1
            prev = 1
        else :
            tmp = sum
            sum += prev
            prev = tmp
        sum %= 10
    return sum

# print(get_fibonacci_last_digit_naive(999999))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
