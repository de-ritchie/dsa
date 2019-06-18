# python3

from collections import namedtuple
import time

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []

    def process(self, request):
        # write your code here
        # time.sleep(1)
        arrived_at = getattr(request, 'arrived_at')
        time_to_process = getattr(request, 'time_to_process')
        if len(self.finish_time) == 0 :
            self.finish_time.append(arrived_at + time_to_process)
            return Response(False, arrived_at)
        else :
            i = 0
            lastFinish = 0
            while len(self.finish_time) > 0 :
                if arrived_at >= self.finish_time[i] :
                    lastFinish = self.finish_time.pop(0)
                else :
                    break
            if len(self.finish_time) > 0 and arrived_at < self.finish_time[-1] :
                if len(self.finish_time) == self.size :
                    return Response(True, -1)
                else :
                    prev = self.finish_time[-1]
                    self.finish_time.append(prev + time_to_process)
                    return Response(False, prev)
            else :
                # self.finish_time = []
                self.finish_time.append(arrived_at + time_to_process)
                return Response(False, arrived_at)

def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
