import csv

# Define Function
def intcode(file, num1, num2):
    # Open csv, make sure I'm reading it as a list
    input = open(file)
    reader = csv.reader(input)
    data = list(map(int, list(reader)[0]))

# Look at each slice of 4 positions
    data[1] = num1
    data[2] = num2
    n = 0
    while n < len(data):
        slice = data[n : n + 4]

    # Look at position 0 of slice
    # If 1, add values in positions 1 and 2, place where directed by postion 3
        if slice[0] == 1:
            data[slice[3]] = data[slice[1]] + data[slice[2]]
            n += 4
    # If 2, multipy values in positions 1 and 2, place where directed by postion 3
        elif slice[0] == 2:
            data[slice[3]] = data[slice[1]] * data[slice[2]]
            n += 4
    # If 99, terminate program and return list
        elif slice[0] == 99:
            return(data[0])
            break
    # If anything besides 1, 2, 99, return Error
        else:
            print('Error, this isn\'t a legitimate code')

        
# Part 1: Write code to find value at position 0 for inputs of 12 and 2
# intcode('input.csv', 12, 2)

# Part 2: Write code to search for inputs that give result of 19690720
GOAL = 19690720
for i in range(100):
    for j in range(100):
        if intcode('input.csv', i, j) == GOAL:
            print(100 * i + j)
            break

