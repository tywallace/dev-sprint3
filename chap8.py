# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Tyler

def rot13(string):
	new_string = ""
	for x in string:
		if ord(x) < 91 and ord(x) > 64:
			y = chr(((ord(x)-65 + 13) % 26) + 65)
		elif ord(x) < 123 and ord(x) > 96:
			y = chr(((ord(x)-97 + 13) % 26) + 97)
		else:
			y = x
		new_string = new_string + y
	return new_string

rot13("HeLlo")

f = open('Rot13Test.txt', 'r')
d = open('Decoded.txt', 'w')


for line in f:
 	l = line
 	new_line = ""
 	for word in l.split():
 		new_line = new_line + rot13(word) + " "
 	d.write(new_line + "\n")




