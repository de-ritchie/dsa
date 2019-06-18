# python3

import sys
import threading

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

def createTree(nodes) :
    root = None
    for node in nodes :
        if node.val == -1:
            root = node
        else :
            nodes[node.val].children.append(node)
    return root

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    nodes = []
    for i in parents :
        nodes.append(Node(i))
    root = createTree(nodes)

    # queue = [root]
    # while len(queue) > 0 :
    #     node = queue.pop(0)
    #     if len(node.children) > 0 :
    #         queue.extend(node.children)
    #     print(node.val)

    if root == None :
        return max_height
    else :
        queue = [0, root]
        prev = 0
        while len(queue) > 0 :
            node = queue.pop(0)
            if isinstance(node, Node) :
                if len(node.children) > 0:
                    queue.extend(node.children)
            else :
                max_height = max(max_height, prev)
                prev = node + 1
                if len(queue) > 0:
                    queue.append(prev)
    
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
