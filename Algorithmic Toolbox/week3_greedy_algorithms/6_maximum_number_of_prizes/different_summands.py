# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    last = 1
    while n > 0 :
        diff = n - last
        if diff >= 0 and diff > last :
            summands.append(last)
            n = diff
        else :
            summands.append(n)
            n = 0
        last += 1
    return summands

# summands = optimal_summands(11)
# print(len(summands))
# for x in summands:
#     print(x, end=' ')

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
