def calculate_string_len(input_string):
	length = len(input_string)
	return length

def get_words(string):

	return string[:2]+string[-2:]

def get_minimum(numbers):
	minimum = numbers[0]
	for num in numbers:
		if num < minimum:
			minimum = num
	return minimum

def get_maximum(numbers):
	maximum = numbers[0]
	for num in numbers:
		if num > maximum:
			maximum = num
	return maximum

def odd(words):

	output =" "

	for i in words:

		if i % 2 == 1:

			output += words[i]

	return output
















					