# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    i1 = i2 = -1
    for i in range(n):
        if i1 < 0 or numbers[i1] < numbers[i] :
            i1 = i
    for i in range(n):
        if i != i1 :
            if i2 < 0 or numbers[i2] < numbers[i] :
                i2 = i
    if i1!=-1 and i2!=-1 :
        return numbers[i1] * numbers[i2]
    else :
        return 0

# print(max_pairwise_product([1,2,3]))

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
