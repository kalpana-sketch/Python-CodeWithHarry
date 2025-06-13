#Strings are immutable
a = "!!! Harry!! !!!!! Harry!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry", "John"))
print(a.split(" "))

blogHeading = "intrOduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))
print(str2.index("is"))

str3 = "WelcomeToTheConsole"
print(str3.isalnum())
print(str3.isalpha())

str4 = "hello world"
print(str4.islower())

str5 = "We wish you a Merry Christmas\n"
print(str5.isprintable())

str6 = "     " #using Spacebar
print(str6.isspace())

str7 = "        " #Using Tab
print(str7.isspace())

str8 = "World Health Organization"
print(str8.istitle())

str9 = "To kill a Mocking bird"
print(str9.istitle())

str10 = "Python is an Interpreted Language"
print(str10.startswith("Python"))
print(str10.swapcase())

print(str2.title())