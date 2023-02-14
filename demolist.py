colors = ["red","green","blue"]
print(colors)

colors.append("white")
print(colors)
colors.append("black")
print(colors)

colors.insert(1,'yellow')

colors += ['red']
print(colors)

print(colors.index("red"))
print(colors.count("red"))

colors += 'red'
print(colors)

print(colors.pop())
print(colors.pop())
print(colors.pop())
print(colors.pop(1))

print(colors)

colors.remove("red")
print(colors)

colors.insert(1,'red')
print(colors)

colors.pop(-1)
print(colors)

colors.reverse()
print(colors)

