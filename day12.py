fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)

print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit) - 3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz:
nm = "Harry"
print(nm[-4:-2]) #-4:-2 => len(nm)-4:len(nm)-2 => 5-4:5-2 => 1:3 => ar  as 1 is included but 3 is not 