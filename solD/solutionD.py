import sys
import math

PI = math.pi


def solve(case_number, area):
    print(case_number)
    print(area)
    # center of the faces
    x_center = [0.5, 0, 0, 1]
    y_center = [0, 0.5, 0, 1]
    z_center = [0, 0, 0.5, 1]
    normal = [0, 1, 0, 1]

    dot_x = dotProduct(x_center[:3], normal[:3])
    if dot_x != 0:
        a = module(x_center[:3]) * module(normal[:3]) / dot_x
    else:
        a = PI/2

    dot_y = dotProduct(y_center[:3], normal[:3])
    if dot_y != 0:
        b = module(y_center[:3]) * module(normal[:3]) / dot_y
    else:
        b = PI/2

    dot_z = dotProduct(z_center[:3], normal[:3])
    if dot_z != 0:
        c = module(z_center[:3]) * module(normal[:3]) / dot_z
    else:
        c = PI/2
    # deviation respect to the normal vector y
    proj_area = area_calc(a, b, c)
    if proj_area < area:
        # rotate around one axis
        rot_x = rotX(PI/4)
        x_center = matrix_mult(rot_x, x_center)
        y_center = matrix_mult(rot_x, y_center)
        z_center = matrix_mult(rot_x, z_center)

    print(x_center[:3])
    print(y_center[:3])
    print(z_center[:3])

    #     # rotate
    # b += PI/4
    # # new area
    # rot_x = rotX(a)
    # rotation_matrix = matrix_mult(rot_x, x_center)
    # x_center = rotation_matrix[:3]
    # print(x_center)
    return "Case #"+str(case_number + 1)+": " + str(proj_area)


def module(vector):
    result = 0
    for vect in vector:
        result += vect ** 2
    return result


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
    return abs(math.cos(a)) + abs(math.cos(b)) + abs(math.cos(c))


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
