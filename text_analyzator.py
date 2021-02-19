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
if num_text == 1 or num_text == 2 or num_text == 3:
	text = TEXTS[num_text - 1]
else:
	sys.exit("Not supported.")
separator()

# STATISTICS
# Number of words in the text
num_words = len(text.strip().split(" "))
print(f"There are {num_words} in the selected text.")

# Number of titlecase words
titlecase_words = []
for word in text:
	if word.istitle() == True:
		titlecase_words.append(word)
titlecase_words = len(titlecase_words)
print(f"There are {titlecase_words} titlacase words.")

# Number of uppercase words
uppercase_words = []
for word in text:
	if word.isupper() == True:
		uppercase_words.append(word)
uppercase_words = len(uppercase_words)
print(f"There are {uppercase_words} uppercase words.")

# Number of lowercase words
lowercase_words = []
for word in text:
	if word.islower() == True:
		lowercase_words.append(word)
lowercase_words = len(lowercase_words)
print(f"There are {lowercase_words} lowercase words.")

# Number of numeric strings
numeric_strings = []
for number in text.split():
	if number.isdigit():
		numeric_strings.append(number)
num_numeric_strings = len(numeric_strings)
print(f"There are {num_numeric_strings} numeric strings.")

# Sum of all numbers
all_number_sum = 0
for number in numeric_strings:
	all_number_sum += int(number)
print(f"The sum of all numbers is {all_number_sum}.")
separator()

# List of words without dots, commas, numbers, space and big letters
words = text.lower()
words = words.replace(".", "")
words = words.replace(",", "")
words = words.replace("?", "")
words = words.split()

for word in words:
	if word.isdigit():
		words.remove(word)

# Dictionary of words and how many times they are in the text
counts = {}
for word in words:
	counts[word] = counts.setdefault(word, 0) + 1

# GRAPH
# data = {length of word: occurence as list}
data = {}
for key, value in counts.items():
	if len(key) not in data:
		data[len(key)] = [value]
	else:
		data[len(key)].append(value)

# data_graph = {length of word: total occurence}
data_graph = {}
for key, value in data.items():
	data_graph[key] = sum(value)

# graph
highest = int(max(data_graph.keys())) + 1
print("LEN|  OCCURENCES" + (int(max(data_graph.values())) - 10) * " " + "|NR.")
separator()
for number in range(1, highest):
	stars = None
	if number in data_graph.keys():
		stars = "*" * data_graph[number]
	else:
		stars = ""
	nr = None
	if number in data_graph.keys():
		nr = data_graph[number]
	else:
		nr = ""

	print((3 - len(str(number))) * " " + str(number) + "|" + stars + 
		((int(max(data_graph.values())) - len(stars)) * " ") + 2 * " " + str(nr))
