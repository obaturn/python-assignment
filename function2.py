def get.words(string)

	words. = string.split()

	first_two_words = " " joins(words[:2])

	second_two_words = " " joins(words[-2:])

	return first_two_words , second_two_words