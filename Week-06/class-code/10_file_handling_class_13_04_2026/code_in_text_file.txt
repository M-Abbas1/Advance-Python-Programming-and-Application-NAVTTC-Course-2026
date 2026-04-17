
text_file = open(r'files\temp.txt', 'r')

text = text_file.read()

print("TYPE OF TEXT VARIABLE : ", type(text))

print(text)

text_file.close()


