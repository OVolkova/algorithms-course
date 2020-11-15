# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_ in enumerate(text):
        if next_ in "([{":
            # Process opening bracket
            opening_brackets_stack.append((next_, i))

        if next_ in ")]}":
            # Process closing bracket
            if opening_brackets_stack:
                opened, open_i = opening_brackets_stack[-1]
                opening_brackets_stack.pop()
                if not are_matching(opened, next_):
                    return i + 1
            else:
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0][1]+1

    return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
