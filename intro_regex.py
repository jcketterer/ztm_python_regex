import re

# pattern = re.compile(r"([a-zA-Z]).([a])")
# string = 'search this inside of this text please! Andrei'

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
# d = pattern.match(string)
# print(a.group())


pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]")
string = 'test1234123_%@cox.com'

a = pattern.search(string)
print(a)