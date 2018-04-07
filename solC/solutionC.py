import sys


def one_empty_surrounding(state, x, y):
    # if the matrix around a point has already been done,
    # skip it
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            x_test = x + i
            y_test = y + j
            if (x_test, y_test) not in state:
                return True
    return False


number_of_tests = int(input())

for test in range(0, number_of_tests):
    done = False
    area = int(input())

    blocks = area // 9

    direction = 'y'
    x, y = 2, 2
    state = set()
    while not done:
        block = 1
        # check whether or not to give the command:
        # if all 9 cells around the decided point are covered,
        # skip it
        while one_empty_surrounding(state, x, y) and not done:
            # give a command to gopher
            print(x, y)
            sys.stdout.flush()
            # response from gopher
            response = input().split()
            i, j = [int(elem) for elem in response]
            state.add((i, j))
            # terminate?
            if [i, j] == [-1, -1]:
                exit()
            elif [i, j] == [0, 0]:
                done = True
        if direction == 'y':
            y += 2
            block += 1
            if block >= blocks:
                direction = 'x'
        elif direction == 'x':
            x += 2
            y = 2
            direction = 'y'

exit()
