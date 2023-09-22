def power(r, n):
    if n > 1:
        return r * power(r, n - 1)
    else:
        return r 

print(power(2, 3))