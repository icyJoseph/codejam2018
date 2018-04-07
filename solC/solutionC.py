import sys


def flusher(x, y):
    print(x, y)
    sys.stdout.flush()


def decision(i, j):
    return i + 10, j-10


grid = [1000, 1000]
number_of_tests = int(input())
for test in range(0, number_of_tests):
    area = int(input())
    flusher(10, 10)
    i, j = [int(elem) for elem in input()]
    x, y = decision(i, j)
    flusher(x, y)
