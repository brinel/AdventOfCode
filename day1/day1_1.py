import csv

def fuel_calc(input):
  x = open(input)
  input = csv.reader(x)
  fuel = 0
  for mass in input:
    fuel = fuel + (int(mass[0]) // 3 - 2)
  print(fuel)

fuel_calc('inputs_mass.csv')
