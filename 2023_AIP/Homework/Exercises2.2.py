setence = input('Enter a sentence : ')
word1 = input('Enter word to replace : ')
word2 = input('Enter replacement word : ')

# replaced = setence.replace(word1, word2)


words = setence.split()
replaced = []

for w in words:
    if w == word1:
        w = word2
    replaced.append(w)

replaced = ' '.join(replaced)
print(replaced)
