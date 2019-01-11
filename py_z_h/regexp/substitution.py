import re

str = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r"(Mr\.|Ms\.|Mrs\.) ([a-z])[a-z]+",re.I)

str = pattern.sub("REDACTED", str)
print(str)


str = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"
pattern = re.compile(r"(Mr\.|Ms\.|Mrs\.) ([a-z])[a-z]+",re.I)
str = pattern.sub(r"\g<1> \g<2>", str)
print(str)


titles = [
 'Babycackes (1978)',
 'Significant others (2018)',
 'Tales of The city (1987)',
]

patt = re.compile(r"(?P<title>[\w\s]+) \((?P<year>\d{4})\)")

for i, t in enumerate(titles):
    titles[i] = patt.sub("\g<year> - \g<title>", t)

# titles = map(lambda t: patt.sub(r"\g<year> - \g<title>", t),titles)

print(sorted(list(titles)))


