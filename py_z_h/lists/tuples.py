# a = b = c = 12
# print(b)
# print(a == b == c)
#
# st = "my " "nice " "string"
# print(st)
#
# tup = "First " "Second ", "Third "
#
# print("="*40)
#
# print(tup)
# print(type(tup))
# # print(tup[0])
#
# tup = tup[0], "bob", tup[1]
#
# fist, second, third = tup
# print(second)
#
# my_list = [1, 2, 3]
# a, b, c = my_list
#
# print(b)
#
# my_tup = my_list[0], 9, my_list[1]
# print(type(my_tup))
# print(my_tup)
#

imelda = "More Mayhem", "Imelda Bla", 1988, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Whatsoever"))

# print(imelda[3])  # tuple of tuples

# imelda[3].append((4,"Bla bla")) # error
# print(imelda)

imelda1 = "More Mayhem", "Imelda Bla", 1988, ([
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Whatsoever")])

print(type(imelda1[3]))  # now it is list

imelda1[3].append((4, "Bla bla"))
# print(imelda1)

title, artist, year, tracks = imelda1
tracks.append((5, "Appended to unpacked"))

print(imelda1)
