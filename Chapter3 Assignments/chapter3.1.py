passed = 0
fail = 0
total= 0 

while True :
	user_input = int(input("enter any number"))

	if user_input == 1:
		passed = passed + 1
	if user_input == 2:
		fail = fail + 1
	if user_input > 2:
		break
total += user_input
print(f' the failure is: {fail}\n and the passed is: {passed}')


