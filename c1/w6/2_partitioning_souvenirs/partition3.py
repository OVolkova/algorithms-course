# Uses python3
import sys


class PartitionNotPossible(Exception):
    pass


def get_indexes_with_sum_of_value(value, objects):
    # if value is in the objects, return it's index
    for i, v in enumerate(objects):
        if v == value:
            return [i]
    # if value was not found in objects, then iterate through objects
    # and make a recursive call with smaller set of objects and value
    # result indexes that gives sum of initial value should be appended as lists
    for i, v in enumerate(objects):
        if value - v > 0:
            try:
                indexes = get_indexes_with_sum_of_value(value - v, [o for k, o in enumerate(objects) if k != i])
                if indexes:
                    indexes = [ind if ind < i else ind+1 for ind in indexes]
                    return [i] + indexes
            except PartitionNotPossible:
                continue

    # if none of recursive calls has found indexes of objects that gives value in sum:
    raise PartitionNotPossible


def partition3(objects, num_objects=3):
    sum_objects = sum(objects)
    if sum_objects % num_objects != 0:
        return 0
    value = sum_objects // num_objects
    # sort objects in reverse order to start with the biggest numbers
    objects = sorted(objects, reverse=True)
    # if even one object is grater then value - partitioning is not possible
    if objects[0] > value:
        return 0

    # loop by all objects num_objects-1 times with returns to the zero's iteration
    # to try to construct value from all objects num_objects-1 times
    # (if it is possible to find this value num_objects-1 times in a sequence,
    #  so it is possible to find it one more time fo sure.)
    num_indexes = []
    excluded_indexes = []
    iteration = 0
    while iteration < num_objects-1:
        try:
            if iteration == 0:
                # on zero iteration - exclude objects, that gives sum of value
                # but left objects do not
                not_used_objects = [o for i, o in enumerate(objects) if i not in excluded_indexes]
            else:
                # on next iteration - exclude objects that were used to construct sum of value on zero's iteration
                not_used_objects = [o for i, o in enumerate(objects) if i not in num_indexes]

            # find which indexes from objects can give sum of value
            indexes = get_indexes_with_sum_of_value(value, not_used_objects)

            if iteration == 0:
                # update indexes with excluded objects to build num_indexes for the next iteration
                for i in excluded_indexes:
                    indexes = [ind if ind < i else ind + 1 for ind in indexes]
                num_indexes = indexes
            iteration += 1

        except PartitionNotPossible:
            if not num_indexes:
                # if partition is not possible on zero's iteration - so it is not possible at all
                return 0
            else:
                # otherwise - update excludes indexes and reset num_indexes and iterations
                iteration = 0
                excluded_indexes.append(num_indexes[-1])
                num_indexes = []
                # partitioning is not possible, if all objects are excluded from zero's iteration
                if len(excluded_indexes) == len(objects):
                    return 0

    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

