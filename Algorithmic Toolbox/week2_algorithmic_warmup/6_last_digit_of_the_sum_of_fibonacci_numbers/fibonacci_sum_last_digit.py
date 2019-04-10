# Uses python3
import sys

def fibonacci_sum_naive(n):
    total = sum = prev = 0
    totalArr = [0]; result = 0
    for i in range(n):
        if i == 0 or i == 1:
            sum = 1
            prev = 1
        else :
            tmp = sum
            sum += prev
            prev = tmp
        sum %= 10
        total += sum
        total %= 10
        result = total
        totalArr.append(total)
        if i == 58 :
            result = totalArr[n % 60]
            break
    # print(totalArr)
    return result

# print(fibonacci_sum_naive(832564823476))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
