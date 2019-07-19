# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     result = []
#     next_free_time = [0] * n_workers
#     for job in jobs:
#         next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#         print("===+{}".format(AssignedJob(next_worker, next_free_time[next_worker])))
#         result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job

#     return result

class PQueue:

    def __init__(self) :
        self.data = []
        self.n = 0

    def peek(self) :

        if self.size() > 0:
            return self.data[0]
    def parent(self, i) :
        return (int)((i - 1)/2)

    def leftChild(self, i) :
        return (2*i) + 1

    def rightChild(self, i) :
        return (2*i) + 2

    def size(self) :
        return self.n

    def computeLength(self) :
        return ((int)(self.size()/2))-1
        
    def add(self, pData) :

        if len(self.data) <= self.n :
            self.data.append(pData)
        else: 
            self.data[self.size()] = pData
        # print("===={}".format(self.size()))
        self.siftUp(self.size())
        self.n += 1

    def extractMin(self) :
        if self.size() > 0:
            minValue = self.data[0]
            self.data[0] = self.data[self.size() - 1]
            self.n -= 1
            self.siftDown(0)
            return minValue
        else:
            return -1

    def siftUp(self, i) :
        
        while i > 0 and self.data[self.parent(i)][0] > self.data[i][0] :
            
            tmp = self.data[i]
            self.data[i] = self.data[self.parent(i)]
            self.data[self.parent(i)] = tmp
            i = self.parent(i)

    def siftDown(self, i) :
        
        if i >= self.size() :
            return
        
        lc = self.leftChild(i)
        rc = self.rightChild(i)
        minIndex = i

        if lc < self.size() and self.data[lc][0] < self.data[minIndex][0] :
            minIndex = lc
        if rc < self.size() and self.data[rc][0] < self.data[minIndex][0] :
            minIndex = rc
        
        if i != minIndex :
            tmp = self.data[minIndex]
            self.data[minIndex] = self.data[i]
            self.data[i] = tmp
            self.siftDown(minIndex)

    def build_heap(self, data):

        self.data = data
        self.n = len(data)
        length = self.computeLength()
        for i in range(length, -1, -1) :
            self.siftDown(i)

def assign_jobs(n_workers, jobs):

    result = []
    t = 0
    # print("Lets roll...!")
    threadQueue = PQueue()
    timeQueue = PQueue()
    for i in range(n_workers):
        threadQueue.add([i, 0])

    while len(jobs) > 0 :

        if t > 0 and timeQueue.size() > 0 :
            
            prevTime, thread = timeQueue.extractMin()
            threadQueue.add([thread, prevTime])
            while timeQueue.size() > 0:
                if timeQueue.peek()[0] == prevTime :
                    prevTime, thread = timeQueue.extractMin()
                    threadQueue.add([thread, prevTime])
                else: 
                    break
        
        while len(jobs) > 0 and threadQueue.size() > 0:
                
            job = jobs.pop(0)
            thread = threadQueue.extractMin()
            timeQueue.add([thread[1] + job, thread[0]])
            # print("Thread {} job {}".format(thread, job))
            result.append(AssignedJob(thread[0], thread[1]))

        t += 1

    return result

def main():
    ip1 = input()
    n_workers, n_jobs = map(int, ip1.split())
    ip2 = input()
    jobs = list(map(int, ip2.split()))
    assert len(jobs) == n_jobs
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
