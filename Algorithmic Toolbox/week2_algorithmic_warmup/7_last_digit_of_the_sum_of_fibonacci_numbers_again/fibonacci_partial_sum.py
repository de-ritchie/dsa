# Uses python3
import sys

def sumOfFiboSeries(from_, to, sumArr):

    result = 0
    for i in range(from_, to) :
        result += sumArr[i%60]
        result %= 10
    return result

def fibonacci_partial_sum_naive(from_, to):

    n = to
    total = sum = prev = 0
    sumArr = [0]
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
        sumArr.append(sum)
        if i == 58 :
            break
    # print(total)
    bound = to - from_ + 1
    upBound = bound % 60
    # print(upBound)
    lowBound = to - upBound + 1
    # print(bound, lowBound, upBound, sumArr)
    a = ((bound // 60) * total)
    # print(bound, total, a)
    a %= 10
    b = sumOfFiboSeries(lowBound, lowBound + upBound, sumArr)
    # print(a, b)
    result = a + b
    return result

# print(fibonacci_partial_sum_naive(10, 200))

if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))