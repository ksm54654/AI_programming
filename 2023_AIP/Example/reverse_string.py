word = input('Enter a word : ')
reversedWord = ''

# for ch in word:
#     reversedWord = ch + reversedWord
# print(reversedWord)

# 처음부터 끝까지 가는데 거꾸로 가라
print(word[::-1])


print(list(reversed(word)))
# print(''.join(list(reversed(word))))

# abcde -> abced
print(word[:-2], end='')
print(word[-1], end='')
print(word[-2], end='')

w = word[:-2] + word[-1:-3:-1]
