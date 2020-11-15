# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.in_buffer = 0
        self.prev_time_index = 0

    def process(self, request: Request):
        current_time = request.arrived_at
        while self.prev_time_index < len(self.finish_time)\
                and self.finish_time[self.prev_time_index] <= current_time:
            self.prev_time_index += 1
            self.in_buffer -= 1

        if self.in_buffer >= self.size:
            return Response(True, -1)
        else:
            if self.finish_time:
                start_time = max(self.finish_time[-1], current_time)
            else:
                start_time = current_time
            self.finish_time.append(start_time + request.time_to_process)
            self.in_buffer += 1

        return Response(False, start_time)


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
