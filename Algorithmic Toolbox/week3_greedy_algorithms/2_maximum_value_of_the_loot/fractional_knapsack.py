# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    ratio = []
    for i in range(len(values)) :
        map = {
            "value": values[i],
            "weight": weights[i],
            "ratio": values[i]/weights[i]
        }
        ratio.append(map)
    # print(ratio)
    ratio.sort(key=lambda x: x['ratio'], reverse=True)
    # print(ratio)
    for i in range(len(values)) :
        
        dictWeight = ratio[i]['weight']
        dictValue = ratio[i]['value']
        diff = capacity - dictWeight
        if diff >= 0 :
            value += dictValue
            capacity = diff
        else :
            value += capacity * ratio[i]['ratio']
            capacity = 0
        

    return value

# print("{:.4f}".format(get_optimal_value(10, [30], [500])))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))