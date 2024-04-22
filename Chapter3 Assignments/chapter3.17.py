gallons_used = 0
miles_driven = 0
per_galon = 0
sentinel_value = -1
counter = 0
miles_driven = float(input("enter the miles driven"))
gallons_used = float(input("enter the gallons used"))
while counter == -1:
	miles_driven = float(input("enter the miles driven (-1 to end)"))
	per_galon = miles_driven / gallons_used
print(f' the miles per galon used is {per_galon}')

