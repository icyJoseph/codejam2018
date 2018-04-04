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
    return ['dummy', 'dummy2']


filename = "example.in"
problem = read_input(filename)
output = process(problem)
print_output(filename, output)
