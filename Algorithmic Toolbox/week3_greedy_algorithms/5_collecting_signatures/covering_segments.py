# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    i = 0
    while i < len(segments) :
        j = i + 1
        while j < len(segments) :
            # startA = segments[i]['start'] #s.start
            endA = segments[i].end
            # startB = segments[j]['start'] #s.start
            endB = segments[j].end
            if endA > endB :
                tmp = segments[i]
                segments[i] = segments[j]
                segments[j] = tmp
            j += 1
        i += 1
    print(segments)
    lowerEnd = 0
    for i in segments :
        start = i.start
        end = i.end
        if len(points) == 0 :
            # print(segments)
            points.append(end)
            lowerEnd = end
        else :
            if start <= lowerEnd and end >= lowerEnd :
                pass
            elif start > lowerEnd :
                points.append(end)
                lowerEnd = end

    return points

# map1 = {"start": 1, "end": 3}
# # map2 = {"start": 1, "end": 3}
# map3 = {"start": 2, "end": 5}
# map4 = {"start": 3, "end": 6}
# arr = [map1, map3, map4]

# print(optimal_points(arr))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
