word = input('Enter word translate : ')

word_lower = word.lower()

if word[0] in 'aeiouAEIOU':
    result = word + 'way'
else:
    for i in range(len(word)):
        if word_lower[i] in 'aeiouAEIOU':
            result = word[i:] + word[:i] + 'ay'
            break

print("The word in Pig Latin is {}.".format(result))
