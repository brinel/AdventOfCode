import csv
import logging
logging.basicConfig(level = logging.DEBUG)

# Define Function
def intcode(file):
    # Open csv, make sure I'm reading it as a list
    input = open(file)
    reader = csv.reader(input)
    memory = list(map(int, list(reader)[0]))

    # TODO: Change this code to loop through all possibilities 0-99 for noun and verb
    noun = 0
    verb = 0
    data = [0]
    logging.debug('noun should be 0, verb 0, data list [0]. They are: ' + str(noun) + str(verb) + str(data))
    
    #while data[0] != 19690720:
     #   data = memory
      #  logging.debug('Data should be the full, original input. It is: ' + str(data))
    while data[0] != 19690720:
        for noun in range(0,100):
            for verb in range(0,100):
                data = memory
                data[1] = noun
                data[2] = verb
                logging.debug('Data should now be the initial list, with positions 1 and 2 replaced. It is: ' + str(data))
                n = 0
                
                while n < len(data):
                    slice = data[n : n + 4]

                # Look at position 0 of slice
                # If 1, add values in positions 1 and 2, place where directed by postion 3
                    if slice[0] == 1:
                        data[slice[3]] = data[slice[1]] + data[slice[2]]
                        n += 4
                # If 2, multiply values in positions 1 and 2, place where directed by postion 3
                    elif slice[0] == 2:
                        data[slice[3]] = data[slice[1]] * data[slice[2]]
                        n += 4
                # If 99, terminate program and return list
                    elif slice[0] == 99:
                        return(data)
                        break
                # If anything besides 1, 2, 99, return Error
                    else:
                        print('Error, this isn\'t a legitimate code')

    answer = (100 * noun) + verb
    print('Noun is %d, verb is %d, and the answer is %d.' % (noun, verb, answer))
        
# Run Function
intcode('input.csv')
