import sys


def solve(case_number, case):
    shield_string, instructions = case
    shield = int(shield_string)
    instructions_arr = [instruction for instruction in instructions]
    shield_breaks = robot_wins(instructions_arr, shield)
    changes = 0
    while shield_breaks:
        previous_instructions = instructions_arr[:]
        hack_robot(instructions_arr)
        changes += 1
        shield_breaks = robot_wins(instructions_arr, shield)
        if previous_instructions == instructions_arr:
            # no change was possible to the instructions
            if shield_breaks:
                return "Case #"+str(case_number + 1)+": " + "IMPOSSIBLE"
    return "Case #"+str(case_number + 1)+": " + str(changes)


def robot_wins(instructions_arr, shield):
    damage = 1
    for command in instructions_arr:
        if command == 'S':
            shield = shield - damage
            if shield < 0:
                return True
        if command == 'C':
            damage += damage
    return False


def hack_robot(instructions_arr):
    # swap S's
    for index in range(0, len(instructions_arr) - 1):
        command = instructions_arr[index]
        if command == 'C':
            next_command = instructions_arr[index+1]
            if next_command == 'S':
                instructions_arr.pop(index)
                instructions_arr.insert(index, 'S')
                instructions_arr.pop(index+1)
                instructions_arr.insert(index + 1, 'C')
                return instructions_arr


number_of_cases = int(input())
solution = []
for _ in range(0, number_of_cases):
    solution.append(solve(_, input().split()))

for sol in solution:
    print(sol)
    sys.stdout.flush()
