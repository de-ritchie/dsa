# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    sum = prev = 0
    cyclePrevPtr = -1; cycle = 0; result = [0]; mod = 0; answer = 0
    for i in range(n):
        if i == 0 or i == 1:
            sum = 1
            prev = 1
        else :
            tmp = sum
            sum += prev
            prev = tmp
        if i > 0 and cyclePrevPtr == 1 and sum % m == 0 :
            cycle += 1
            mod = n % cycle
            answer = result[mod]
            break
        # print('====mod', sum%m)
        mod = sum % m
        answer = mod
        cyclePrevPtr = mod
        result.append(mod)
        cycle += 1

    # print('mod', mod, n, cycle, result)
    return answer

# print(6, '-----*')
# print(get_fibonacci_huge_naive(2816213588, 239))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
