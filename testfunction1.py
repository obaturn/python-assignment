from function1 import calculate_string_len,get_minimum,get_words, get_maximum,odd


def test_calculate_string_len():
	assert calculate_string_len("semicolon") == 9
	assert calculate_string_len("toluwalase") == 10

def test_get_words():
	assert get_words('semicolon') =='seon'
	assert get_words('toluwalase') =='tose'

def test_getminimum():
	assert get_minimum([8, 4, 9, 2, 5]) == 2
def test_getmaximum():
	assert get_maximum([8, 4, 9, 2, 6]) == 9
def test_odd():
	assert odd('semicolon') =='eioo'







