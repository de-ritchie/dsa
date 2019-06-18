#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0 :
        i = 0
        j = i + 1
        if j == len(a) :
            res += str(a[i])
            break
        while j < len(a) :
            if len(a[i]) == len(a[j]) :
                if int(a[i]) < int(a[j]) :
                    i = j
            else :
                a1 = a[i] + a[j]
                a2 = a[j] + a[i]
                if int(a1) < int(a2) :
                    i = j
            j += 1
        res += a[i]
        del a[i]
        # print(a)
    return res

# print(largest_number(['344', '34']))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
