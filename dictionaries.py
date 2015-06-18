# my_stats = {"name":"Brooke","age":"26","height":"65"}
# print my_stats["name"],"is",my_stats["age"],"years old with a height of",my_stats["height"],"."
# del my_stats["age"]
# print my_stats

# vocabulary_words = {"variable":"placeholder that holds the value", "object": "any value in python", "concatenation":"adding strings together using the plus sign", "boolean":"the answers are always either true or false"}

# def my_name(name):
# 	name_list = {}
# 	for i in name:
# 		name_list[i] = name.count(i)
# 	return name_list

# name = "Brooke"
# print my_name(name)

# def my_string(random_string):
# 	string_list = {}
# 	for i in random_string:
# 		string_list[i] = random_string.count(i)
# 	return string_list

# random_string = "Chelsea"
# print my_string(random_string)

# open file, read and close file
# fish = open("one_fish_two_fish.txt")
# fish_string = fish.read()
# fish.close()

#DICTIONARY PRACTICE NUMBER 5
# Write a program that counts how many times each letter appears in a file. 
# Download the file one_fish_two_fish.txt from the class website 
# to test your program. 
# Return a dictionary.

# #write a function that counts letters in the file
# def practice(fish_string):
# 	letter_dictionary = {}
# 	for i in fish_string:
# 		letter_dictionary[i] = fish_string.count(i)
# 	return letter_dictionary

# print practice(fish_string)


#DICTIONARY PRACTICE NUMBER 6
# Write a program that counts how many times each 
# word appears in a random string. When given 
# one fish two fish red fish blue fish it should 
# return a dictionary



# open file, read and close file
fish = open("one_fish_two_fish.txt")
fish_string = fish.read()
fish.close()

print fish_string

#define a function named "practice" that takes 
#in "fish_string" from above
def practice(fish_string):
#create an empty dictionary to take in the words
	word_dictionary = {}
#parse our string into words, splitting (dividing) it
# on the empty space " "
# and by creating a new variable called fish_word_list
#create a list of words
	fish_string = fish_string.replace( "\n"," ")
	print fish_string
	fish_word_list = fish_string.split(" ")
	for i in fish_word_list:
		word_dictionary[i] = fish_word_list.count(i)
	return word_dictionary

print practice(fish_string)