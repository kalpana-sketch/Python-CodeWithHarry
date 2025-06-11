name = "Kalpana"
friend = "Ridhima"
anotherFriend = "Khushi"

apple = """He said,
Hi Kalpana
hey I am good
"I want to eat an apple"""

print("Hello, " + name)
# print(apple)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
# print(name[7])  #Throws an IndexError

print("Lets use a for loop\n")
for character in name:
    print(character)