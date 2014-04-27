# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Tyler

def rot13(string):
	new_string = ""
	for x in string:
		if ord(x) < 97:
			y = chr(((ord(x)-65 + 13) % 26) + 65)
		else:
			y = chr(((ord(x)-97 + 13) % 26) + 97)
		new_string = new_string + y
	print new_string

rot13("HeLlo")