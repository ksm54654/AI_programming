class Rectangle:
    def __init__(self, width = 1, height=1):
        self._width = width
        self._height = height
        self._secrect = 0 # 무ㅓ지이거 

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def getWidth(self):
        return self._width
    
    def getHeight(self):
        return self._height
    
    def ares(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def __str__(self):
        return ("Width : " + str(self._width) + "\nHeight : " + str(self._height))


rect = Rectangle(5,10)
print(rect)

rect._width = 100 
rect.setWith(100)
print(rect)

print(rect._Rectangle__secret)
print(rect._secret)