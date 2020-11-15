import os
from process_packages import process_requests, Request, Response, Buffer


def iter_tests():
    tests = {}
    for name in sorted(os.listdir('./tests')):
        if name.split('.'):
            tests[name.split('.')[0]] = name
        else:
            tests[name] = None

    for test, answer in tests.items():
        print(test)
        with open(os.path.join('./tests', test), 'r') as file:
            buffer_size, n_requests = map(int, file.readline().split())
            requests = []
            for _ in range(n_requests):
                arrived_at, time_to_process = map(int, file.readline().split())
                requests.append(Request(arrived_at, time_to_process))
            data = (buffer_size, n_requests, requests)

        with open(os.path.join('./tests', answer), 'r') as file:
            answers = []
            for _ in range(n_requests):
                answers.append(int(file.readline()))

        yield data, answers


def main():
    test = iter_tests()
    i = 0
    iterate = True
    while iterate:
        try:
            data, result = next(test)
            buffer = Buffer(data[0])
            responses = process_requests(data[2], buffer)
            result_responses = [response.started_at if not response.was_dropped else -1 for response in responses]
            print(i, result == result_responses)
            if result != result_responses:
                print(result)
                print(result_responses)

            assert result == result_responses
            i += 1
        except StopIteration:
            iterate = False


main()
