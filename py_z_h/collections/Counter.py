from collections import Counter

l = [1,1,1,2,2,2,3,4,8,9]
# print(Counter(l))

str = "aasssssgfdsafgsdfgsdfff"
# print(Counter(str))

str = "How many times each word shows up. Word 1, word 2, show up"

str = str.lower().split()
c = Counter(str)

# print(sum(c.values()))

#print(list(c))  # to list of unique items
#print(set(c))   # to set

#print(dict(c)) # convert to regular dictionary

#print(c.items())  # list of tuples
#print(Counter(dict(c.items())))  # from list of tuples to default counter


#print(c.most_common())  # from  most common to least common
#print(c.most_common()[:-5:-1])  # 5 from the end (5 least common)

c = dict(c)
c["bla"] = -2
print(c)
c = Counter(c)   # transform from dict to counter
c += Counter()  # remove all 0 or negative counts
print(c)

c.clear()  # reset all counts



