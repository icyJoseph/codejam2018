import sys


def check_surrounding(state, x, y):
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
    path = 0
    if area < 100:
        path = area
        folds = area // 2
    else:
        folds = (area // 1000) + 1
        path = 1000
    direction = 'y'
    x, y = 2, 2
    state = set()
    while not done:
        # check whether or not to give the command:
        if check_surrounding(state, x, y):
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
        else:
            if direction == 'y':
                y += 1
                if y >= path + 1:
                    direction = 'x'
            elif direction == 'x':
                x += 1
                y = 2
                direction = 'y'
                if x >= folds:
                    y = 2
                    x = 2
                    direction = 'y'
exit()
