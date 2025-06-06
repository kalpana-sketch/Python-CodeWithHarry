import pandas
import hashlib

print("hi")

df = pandas.read_csv("words.csv")
print(df)

m = hashlib.sha256()