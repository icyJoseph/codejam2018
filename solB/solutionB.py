import sys


def solve(case_number, length, case):
    sol1 = solveA(case_number, length, case)
    sol2 = solveB(case_number, length, case)
    comp = compare(sol1, sol2)
    print(sol1)
    print(sol2)
    print(comp)
    return sol1


def solveA(case_number, length, case):
    numbers = [int(elem) for elem in case]
    dictionary = {}
    copy = numbers[:]
    for index in range(0, length):
        minimum, copy = take_min(copy)
        seed = 0
        if numbers.count(minimum) > 1:
            repeats = numbers.count(minimum)
            flag = True
            i = 0
            while flag:
                if i < repeats:
                    current_index = numbers.index(minimum, seed)
                    if abs(index - current_index) % 2 == 0:
                        dictionary[index] = [minimum, current_index]
                        flag = False
                    seed = numbers.index(minimum, seed)
                    seed += 1
                if i >= repeats:
                    flag = False
                i += 1
        else:
            current_index = numbers.index(minimum)
            dictionary[index] = [minimum, current_index]
        # print(dictionary)
        # print('current_index ' + str(current_index))
        # print('index ' + str(index))
        if abs(index - current_index) % 2 != 0:
            return "Case #"+str(case_number + 1)+": " + str(index)
    return "Case #"+str(case_number + 1)+": " + "OK"


def solveB(case_number, length, case):
    numbers = [int(elem) for elem in case]
    copy = numbers[:]
    copy.sort()
    trouble_sorted = trouble_sort(numbers)
    if copy == trouble_sorted:
        return "Case #"+str(case_number + 1)+": " + "OK"
    failure = test_indeces(copy, trouble_sorted)
    return "Case #"+str(case_number + 1)+": " + str(failure)


def compare(solA, solB):
    return solA == solB


def test_indeces(right, wrong):
    for index in range(0, len(right)):
        if right[index] != wrong[index]:
            return index


def trouble_sort(numbers):
    done = False
    while not done:
        done = True
        for index in range(0, len(numbers) - 2):
            if numbers[index] > numbers[index+2]:
                done = False
                numbers[index+2], numbers[index] = numbers[index], numbers[index+2]
    return numbers


def take_min(numbers):
    copy = numbers[:]
    minimum = min(copy)
    copy.remove(minimum)
    return minimum, copy


def check_sub_list(sub_list):
    copy = sub_list[:]
    copy.sort()
    if copy == sub_list:
        return True
    return False


number_of_cases = int(input())
solution = []
for _ in range(0, number_of_cases):
    incoming_length = int(input())
    solution.append(solveB(_, incoming_length, input().split()))

for sol in solution:
    print(sol)
    sys.stdout.flush()
