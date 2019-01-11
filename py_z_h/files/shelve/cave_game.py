import shelve

map_game = shelve.open('map_game')
locations = map_game['locations']
vocabulary = map_game['vocabulary']

loc = 1
while True:
    av_directions = ", ".join(locations[loc]["exits"])
    print(locations[loc]["desc"])
    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    nex_loc = input("Availiable directions: " + av_directions + " ").upper()
    if len(nex_loc) > 1:
        # for word in vocabulary:
        #     if word in nex_loc:
        #         nex_loc = vocabulary[word]
        words = nex_loc.split()
        for word in words:
            if word in vocabulary:
                nex_loc = vocabulary[word]

    if nex_loc in allExits:
        loc = allExits[nex_loc]
    else:
        print("You cannot go there")

map_game.close()