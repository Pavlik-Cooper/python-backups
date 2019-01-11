import re

# (https?)://([a-zA-Z-_]+)\.([a-zA-Z-_]+/?)

# https://google.com
# https://pythex.org/

# (Mr\.|Mrs\.|Ms\.)(\s\w+\s\w+)
str ="Mr. John Anderson \
Mrs. Julia Smith \
Ms. Julieta Blum"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.)(\s\w+\s\w+)')

# print(pattern.findall(str))
# print(pattern.search(str))

match = re.search(r'(Mr\.|Mrs\.|Ms\.)(\s\w+\s\w+)',str)
# print(match.group())

match = re.findall(r'(Mr\.|Mrs\.|Ms\.)(\s\w+\s\w+)',str)
# print(match)



phone_reg = re.compile(r'\b\d{3} \d{3}-?\d{4}\b')

# match = phone_reg.match("wqer 432 567-4888") // won't match
match = phone_reg.match("432 567-4888 rthtweer")


if match:
    print(match.group())
else:
    print("None")

# re.split()
# re.findall()

