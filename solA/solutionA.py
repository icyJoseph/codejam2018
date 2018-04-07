# Read a given filename
def read_input(filename):
    with open(filename) as file:
        input = file.readlines()
        inputArr = [i.replace("\n", "").split() for i in input]
        return inputArr


# Output a file given a list of strings
# list = ["string", "string", ....]
def print_output(filename, list):
    outputname = filename.split('.')
    output_file = open(outputname[0]+'.out', 'w')
    for element in list:
        output_file.write(element)
        output_file.write('\n')
    output_file.close()
    print("Done.")


# Solution goes here
def process(problem):
    number_of_cases = int(problem[0][0])
    cases = problem[1:]
    solution = [solve(case_number, cases[case_number])
                for case_number in range(0, number_of_cases)]
    return solution


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


filename = "example.in"
problem = read_input(filename)
output = process(problem)
print_output(filename, output)
