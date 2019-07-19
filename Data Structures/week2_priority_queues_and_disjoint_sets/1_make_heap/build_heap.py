# python3


# def build_heap(data):
#     """Build a heap from ``data`` inplace.

#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps

def parent(i) :
    return (i - 1)/2

def leftChild(i) :
    return (2*i) + 1

def rightChild(i) :
    return (2*i) + 2

def computeLength(n) :
    return ((int)(n/2))-1

# def siftUp(i, data) :
    
#     while i > 0 and data[parent(i)] > data[i] :
        
#         tmp = data[i]
#         data[i] = data[parent(i)]
#         data[parent(i)] = tmp
#         i = parent(i)

def siftDown(i, data, swaps) :
    
    if i >= len(data) :
        return
    
    lc = leftChild(i)
    rc = rightChild(i)
    minIndex = i

    if lc < len(data) and data[lc] < data[minIndex] :
        minIndex = lc
    if rc < len(data) and data[rc] < data[minIndex] :
        minIndex = rc
    
    if i != minIndex :
        tmp = data[minIndex]
        data[minIndex] = data[i]
        data[i] = tmp
        swaps.append((i, minIndex))
        siftDown(minIndex, data, swaps)

def build_heap(data):

    swaps = []
    length = computeLength(len(data))
    for i in range(length, -1, -1) :
        siftDown(i, data, swaps)
    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
