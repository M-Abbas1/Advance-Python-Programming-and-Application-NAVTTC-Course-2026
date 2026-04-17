

user_text = input("Enter a text : ")
user_text = user_text.lower()

characters = []
freqs = []

for char in user_text:
    if char not in characters:
        if char.isalpha():
            characters.append(char)
            freqs.append(user_text.count(char))



for i in range(len(characters)):
    print(characters[i], freqs[i])


mind = freqs.index(max(freqs))

print("most commond letter" , characters[mind], freqs[mind])

lest_ind = freqs.index(min(freqs))

print("least commond letter" , characters[lest_ind], freqs[lest_ind])

print(characters)
