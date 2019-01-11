import shelve
import imports

print(__name__)

print("==================")


for x in sorted(globals()):
    print(x)


print(dir())
print(dir(shelve))

for builtin in dir(__builtins__)[::-1]:
    print(builtin)

