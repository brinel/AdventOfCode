import csv


# Original code to calculate fuel needed for just the modules
def fuel_calc(input):
  x = open(input)
  input = csv.reader(x)
  totalFuel = 0

  for mass in input:
    fuel = 0
    modMass = int(mass[0])

    while modMass > 8:
        fuel = fuel + (modMass // 3 - 2)
        modMass = (modMass // 3 - 2)

    totalFuel = totalFuel + fuel

  print(totalFuel)

# TODO: Build loop that calculates fuel needed to launch the fuel


fuel_calc('inputs_mass.csv')
