phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.pop(0)
plist.pop(2)
b = plist.pop(3)
for num in range(4):
    plist.pop()
plist.pop(3)
plist.append('p')
print(plist)