# Uses python3
# 1 1 2 3 5 8
def calc_fib(n):
    sum = prev = 0
    for i in range(n):
        if i == 0 or i == 1:
            sum = 1
            prev = 1
        else :
            tmp = sum
            sum += prev
            prev = tmp
    return sum

n = int(input())
print(calc_fib(n))
