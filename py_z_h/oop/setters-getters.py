from Player import Player


player = Player("beginner")
# player._set_level(15)
# print(player._get_level())

player.level += 2
player.lives += 3
player.score = 500

print(player)


