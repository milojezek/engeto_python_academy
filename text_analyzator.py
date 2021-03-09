import sys

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
		]

def separator():
	print(30 * "-")


# Login
username = input("Username: ")
password = input("Password: ")
registered_users = {
	"bob": "123",
	"ann": "pass123",
	"mike": "password123",
	"liz": "pass123"
}

# Check username and password
if registered_users.get(username) == password:
	separator()
	print("Welcome to the app, " + username)
	print("We have " + str(len(TEXTS)) + " texts to be analyzed.")
	separator()
else:
	sys.exit("It seems you're not a registered user.")

# Choose a text
num_text = int(input("Enter a number between 1 and 3: "))
if num_text in [1, 2, 3]:
	text = TEXTS[num_text - 1]
else:
	sys.exit("Not supported.")
separator()

# STATISTICS
lst = text.split()				# Unclean list of all words
all_words = []					# Clean list
titlecase_words = 0
uppercase_words = 0
lowercase_words = 0
num_strings = 0
all_num_sum = 0

for word in lst:			# Counting all words (numeric strings included)
	all_words.append(word.strip('.,?!:'))
for word in all_words:			# Counting titlecase words
	if word.istitle():
		titlecase_words = titlecase_words + 1
	elif word.isupper():		# Counting uppercase words
		uppercase_words = uppercase_words + 1
	elif word.islower():		# Counting lowercase words
		lowercase_words = lowercase_words + 1
	elif word.isdigit():		# Counting numeric strings
		numeric_strings = num_strings + 1
		all_num_sum += str(word)

print(f"There are {len(all_words) - num_strings} in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {num_strings} numeric strings.")
print(f"The sum of all numbers is {all_num_sum}.")
separator()

counts = []				# Counting word occurence
for word in all_words:
	word = word.lower()
	if not word.isdigit():
		counts.append(len(word))

# GRAPH
print("LEN|  OCCURENCES" + 10 * " " + "|NR.")
for num in range(1, max(counts) + 1):
	print(
		((3 - len(str(num))) * ' ') + str(num) + '|',
		('*' * counts.count(num)),
		((20 - counts.count(num)) * " ") + str(counts.count(num))
	)
