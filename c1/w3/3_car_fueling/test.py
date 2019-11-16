from car_fueling import compute_min_refills


if __name__ == '__main__':

    tests = [(700, 200, [100, 200, 300, 400, 500], 3),
             (700, 200, [100, 200, 300, 400], -1),
             (950, 400, [200, 375, 550, 750], 2),
             (10, 3, [1, 2, 5, 9], -1),
             (200, 250, [100, 150], 0),
             ]

    for test in tests:
        assert test[-1] == compute_min_refills(test[0], test[1], test[2])
