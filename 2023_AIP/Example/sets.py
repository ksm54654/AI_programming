bri = {'brazil', 'russia', 'india'}
print('india' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')
bri.remove('russia')

print(bri)
print(bric)

print(bric.issuperset(bri))
print(bri & bric)
print(bric.difference(bri))
print(bric.union(bri))

print("----------------------------------")

bricc = {'brazil', 'russia', 'india', 'china'}
print(bricc)

print(sorted(bricc))

print(sorted(bricc, key=len, reverse=True))

print(bricc)

print({x * x for x in range(-3, 3)})
