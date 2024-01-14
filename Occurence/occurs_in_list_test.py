from occurs_in_list import occurs_in_list

def test_occurs_in_list():
	fruits = ["apple", "mango", "almond", "currant"]
	fruit = ["peer"]
	assert occurs_in_list(fruits, fruit) == False