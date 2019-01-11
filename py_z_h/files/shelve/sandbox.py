import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]


with shelve.open('sandbox') as sandbox:
    sandbox['blt'] = blt
    sandbox['beans_on_toast'] = scrambled_eggs
    sandbox['soup'] = soup
    # 1) Updating
    tmp_soup = sandbox['soup']
    tmp_soup.append('carrot')
    sandbox['soup'] = tmp_soup

    for recipe in sandbox:
        print(sandbox[recipe])

    print(list(sandbox.items()))

print("=======================")


with shelve.open('sandbox',writeback=True) as sandbox:
    sandbox['blt'] = blt
    sandbox['beans_on_toast'] = scrambled_eggs
    sandbox['soup'] = soup

    # 2) Updating
    sandbox['soup'].append("cucumber")

    for recipe in sandbox:
        print(sandbox[recipe])

    print(list(sandbox.values()))