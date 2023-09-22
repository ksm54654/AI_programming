def isAplha(L):
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True
        
def isAlphaRecursion(L):
    if len(L) <= 1:
        return True
    elif L[0] <= L[1]:
        return isAlphaRecursion(L[1:])
    else:
        return False


list_word1 = ['apple', 'banana', 'carrot']
list_word2 = ['zebra', 'zero', 'alpha']

# print(isAplha(list_word1))
# print(isAplha(list_word2))

print(isAlphaRecursion(list_word1))
print(isAlphaRecursion(list_word2))