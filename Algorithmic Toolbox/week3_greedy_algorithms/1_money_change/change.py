# Uses python3
import sys

def get_change(m):
    #write your code here
    count = 0
    coins = [10, 5, 1]
    n = len(coins)
    i = 0
    while m > 0 and n >= 0 :
        coin = coins[i]
        while coin <= m :
            m -= coin
            count += 1
        i += 1
    return count

# print(get_change(28))

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
