count = 0
total_drivers_gallon = 0
total_miles_driven = 0
drivers_gallon = float(input('Enter the gallon used, -1 t0 end: '))
miles_driven = int(input('Enter the miles driven: '))
while drivers_gallon != -1:
    total_drivers_gallon += drivers_gallon
    total_miles_driven += miles_driven
    count += 1
    miles_per_gallon = miles_driven / drivers_gallon
    print(f'The miles/gallons for this tank was {miles_per_gallon: .2f}')

    miles_driven = int(input('Enter the miles driven: '))
    drivers_gallon = float(input('Enter the gallon used, -1 t0 end: '))


average_miles_per_gallon = total_miles_driven / total_drivers_gallon
print(f'The overall average miles/gallon was {average_miles_per_gallon}')