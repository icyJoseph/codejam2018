import sys


def solve(case_number, case):
    return "Case #"+str(case_number + 1)+": " + str(case_number)


number_of_cases = int(input())
solution = []
for _ in range(0, number_of_cases):
    solution.append(solve(_, input().split()))

for sol in solution:
    print(sol)
    sys.stdout.flush()
