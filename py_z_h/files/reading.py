# file.read() returns all contents at once
# file.readline() # next line on each call
# file.readlines() # returns list of strings (lines)

jaber = open("text.txt","r")
# print(jaber.read())
jaber.seek(0)
# print(jaber.readline())
# print(jaber.readline())
jaber.seek(0)
# print(jaber.readlines())


jaber.seek(0)
for line in jaber:
    if "jabber" in line.lower():
        print(line)

jaber.close()
print(jaber.closed)
#
print("*"*35)
#
# with open("text.txt") as jaber:
#     for line in jaber:
#         print(line)

# with open("text.txt") as jaber:
#     print(jaber.read())

with open("text.txt") as jaber:
    lines = jaber.readlines()

for line in lines:
    print(line, end='')

# for line in lines[::-1]:
#     print(line, end='')
#

# with open("text.txt") as jaber:
#     line = jaber.readline()
#     while line:
#         print(line, end='')
#         line = jaber.readline()


itr = iter("And hast thou slain the Jabberwock?".split())
while itr:
    try:
        print(next(itr))
    except StopIteration:
        break