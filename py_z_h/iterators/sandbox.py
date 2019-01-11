
itr = iter("And hast thou slain the Jabberwock?".split())
while itr:
    try:
        print(next(itr))
    except StopIteration:
        break