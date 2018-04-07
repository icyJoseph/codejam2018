import sys
import math

PI = math.pi


def solve(case_number, area):
    # center of the faces
    x_center = [0.5, 0, 0, 1]
    y_center = [0, 0.5, 0, 1]
    z_center = [0, 0, 0.5, 1]

    # normal vectors
    cos_x_n = cos_N(x_center[:3])
    cos_y_n = cos_N(y_center[:3])
    cos_z_n = cos_N(z_center[:3])

    proj_area = area_calc(cos_x_n, cos_y_n, cos_z_n)

    step = PI / 4

    while abs(proj_area - area) > 1e-06:
        # rotate around one axis
        # print(step)
        rot_x = rotX(step)
        x_center = matrix_mult(rot_x, x_center)
        y_center = matrix_mult(rot_x, y_center)
        z_center = matrix_mult(rot_x, z_center)

        cos_x_n = cos_N(x_center[:3])
        cos_y_n = cos_N(y_center[:3])
        cos_z_n = cos_N(z_center[:3])

        proj_area = area_calc(cos_x_n, cos_y_n, cos_z_n)
        if proj_area > area:
            step = - abs(step / 2)
        elif proj_area < area:
            step = abs(step / 2)
    x_string = vectorString(x_center[:3])
    y_string = vectorString(y_center[:3])
    z_string = vectorString(z_center[:3])

    return "Case #"+str(case_number + 1)+":\n" + x_string + \
        "\n" + y_string + "\n" + z_string


def vectorString(vector):
    copy = vector[:]
    for index in range(0, len(copy)):
        if copy[index] == 0.0:
            copy[index] = '0'
    return ' '.join(str(e) for e in copy)


def cos_N(vector):
    normal = [0, 1, 0]
    dot_p = dotProduct(vector, normal)
    mod = module(vector)
    return dot_p / mod


def module(vector):
    result = 0
    for vect in vector:
        result += vect ** 2
    return math.sqrt(result)


def dotProduct(X, Y):
    return sum(map(lambda pair: pair[0]*pair[1], zip(X, Y)))


def matrix_mult(X, Y):
    result = [0,
              0,
              0,
              0]

    for i in range(len(X)):
        for j in range(len(Y)):
            result[i] += X[i][j] * Y[j]
    return result


def area_calc(a, b, c):
    return abs(a) + abs(b) + abs(c)


def rotX(a):
    return [[1, 0, 0, 0],
            [0, math.cos(a), -math.sin(a), 0],
            [0, math.sin(a), math.cos(a), 0],
            [0, 0, 0, 1]]


def rotY(a):
    return [[math.cos(a), 0, math.sin(a), 0],
            [0, 1, 0, 0],
            [-math.sin(a), 0, math.cos(a), 0],
            [0, 0, 0, 1]]


def rotZ(a):
    return [[math.cos(a), -math.sin(a), 0, 0],
            [math.sin(a), math.cos(a), 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 1]]


number_of_cases = int(input())
solution = []
for _ in range(0, number_of_cases):
    area = float(input())
    solution.append(solve(_, area))

for sol in solution:
    print(sol)
    sys.stdout.flush()
