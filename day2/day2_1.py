import csv

# Define Function
def intcode(file):
    # Open csv, make sure I'm reading it as a list
    input = open(file)
    reader = csv.reader(input)
    data = list(map(int, list(reader)[0]))

# Look at each slice of 4 positions
    data[1] = 12
    data[2] = 2
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
            print(data)
            break
    # If anything besides 1, 2, 99, return Error
        else:
            print('Error, this isn\'t a legitimate code')

        
# Run Function
intcode('input.csv')
