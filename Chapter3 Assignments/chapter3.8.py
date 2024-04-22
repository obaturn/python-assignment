sum = 0
average = 0
product = 1 
largest = 1
smallest = 1000000000

for number in range(4):
	user_input = int(input("enter your numbers"))

	sum += user_input

	product *= user_input

	average = sum / 4

	if user_input > largest:
		largest = user_input

	if user_input < smallest:
		smallest = user_input

print(f'the total number is {sum}:\n and the product is {product}\n and the avearge is: {average}\n and the largest is: {largest}\n and the smallest is: {smallest} ')