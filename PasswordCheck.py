import re

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")

string = "mane232%s2"

#a = pattern.fullmatch(string)

a = pattern.fullmatch(input("Enter password: "))

print(a)