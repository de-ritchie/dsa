# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here

    # print('----')
    numRefill = currRefill = 0
    stops = [0] + stops
    n = len(stops)
    stops.append(distance)
    while currRefill < n :
        lastRefill = currRefill
        # print('----OUTSIDE')
        while currRefill < n and ((stops[currRefill + 1] - stops[lastRefill]) <= tank) :
            # print('----INSIDE')
            currRefill += 1
        if currRefill == lastRefill :
            return -1
        if currRefill < n :
            numRefill += 1
    return numRefill

# print(compute_min_refills(950, 400, [200, 375, 550, 750]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
