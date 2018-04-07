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
    print(case_number)
    x = robot_wins(instructions, shield)
    print(x)
    return "Case #"+str(case_number + 1)+": " + "SOLUTION"


def robot_wins(instructions, shield):
    instructions_arr = [instruction for instruction in instructions]
    damage = 1
    for command in instructions_arr:
        if command == 'S':
            print('shoot with: ' + str(damage) + " to shield: " + str(shield))
            if (damage > shield):
                return True
        if command == 'C':
            damage += damage
    return False


def hack_robot(instructions_arr, left):
    # swap S's
    for index in range(0, instructions_arr):
        command = instructions_arr[index]
        if command == 'S':
            next_command = instructions_arr[index+1]
            if next_command == 'C':
                instructions_arr[index] = 'C'
                instructions_arr[index+1] = 'S'
                return instructions_arr


filename = "example.in"
problem = read_input(filename)
output = process(problem)
print_output(filename, output)
