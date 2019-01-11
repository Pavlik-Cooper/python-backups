import re

reg = re.compile(r"""
(?P<protocol>http://|https://)  # protocol
(?P<domain>(www\.)?[A-za-z-]{2,256}\.[a-z]{2,6})  # domain
(?P<resource_path>[-a-zA-Z0-9@:%_\+.~#?&//=]*)  # path of the resource
""",re.VERBOSE | re.IGNORECASE)

match = reg.match("https://google.com/?foo=bar")
if match:
    print(match.group())
    print(match.group(1))
    print(match.group('protocol'))
    print(match.group('domain'))
    print(match.group('resource_path'))
    print(match.groups())



