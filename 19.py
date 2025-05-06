sentence = input("")
mod_sentence = ""
for char in sentence:
	if char.isalnum() or char.isspace():
		mod_sentence+=char
print(mod_sentence)
