from change import get_change

if __name__ == '__main__':

    tests = [(2, 2), (28, 6), (101, 11), (123, 15), (1012030410, 101203041), (1012030415, 101203042)]
    for test in tests:
        assert test[1] == get_change(test[0])
