shopList = ['apple', 'mango', 'game', 'car']

myList = shopList
copiedList = shopList[:]

del myList[0]

print(shopList)
print(myList)
# 주소가 같아서 같은값이 나옴, 
print(copiedList)

print(id(shopList))
print(id(myList))
print(id(copiedList))