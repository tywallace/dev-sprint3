# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Tyler


fin = open('words.txt')
print fin

line = fin.readline()

#9.1
def twenty_char():
	twenty_char_list = []
	for line in fin:
		word = line.strip()
		if len(word) > 20:
			twenty_char_list.append(word)
	return twenty_char_list

#9.2

def has_no_e():
	has_no_e_list = []
	for line in fin:
		word = line.strip()
		if 'e' not in word:
			has_no_e_list.append(word)
	return has_no_e_list

#9.3
def avoids(word,letters):
	x = 0
	flag = True
	while x < len(letters):
		if letters[x] in word:
			flag = False
		x = x + 1
	return flag


#9.4
def contains(word,letters):
	x = 0
	flag = True
	while x < len(letters):
		if letters[x] not in word:
			flag = False
		x = x + 1
	return flag

print contains("bacdd","abcd")

#acefhlo
#hello face
