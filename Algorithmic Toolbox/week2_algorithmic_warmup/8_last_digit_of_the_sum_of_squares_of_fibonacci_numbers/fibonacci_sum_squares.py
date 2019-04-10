# Uses python3
from sys import stdin

def sumOfFiboSeries(from_, to, sumArr):

    result = 0
    for i in range(from_, to) :
        result += sumArr[i%60] * sumArr[i%60]
        result %= 10
    return result

def fibonacci_sum_squares_naive(n):

    total = sum = prev = 0
    sumArr = [0]
    totalArr = [0]
    for i in range(n):
        if i == 0 or i == 1:
            sum = 1
            prev = 1
        else :
            tmp = sum
            sum += prev
            prev = tmp
        sum %= 10
        total += (sum * sum)
        total %= 10
        sumArr.append(sum)
        totalArr.append(total)
        if i == 58 :
            break
    from_ = 0
    to = n
    bound = to - from_ + 1
    upBound = bound % 60
    lowBound = to - upBound + 1
    # print(lowBound, upBound)
    a = ((bound // 60) * total)
    a %= 10
    b = sumOfFiboSeries(lowBound, lowBound + upBound, sumArr)
    # print(total, sumArr, totalArr, a, b)
    return a + b

# print(fibonacci_sum_squares_naive(1234567890))

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
