import random
class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_hit_points = self.hit_points - damage
        if remaining_hit_points >= 0:
            self.hit_points = remaining_hit_points
            print(f"{self.name} took {damage} points damage and have {self.hit_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} took {damage} points damage and have {self.hit_points} left")
                print(f"{self.name} lost a life")
            else:
                print(f"{self.name} is dead")
                self.lives = 0
                self.alive = False

    def __str__(self):
        return "Name: {0.name}, Hit Points: {0.hit_points}, Lives: {0.lives}".format(self)


class Troll(Enemy):
    def __init__(self, name="troll", hit_points=0, lives=1):
        # Enemy.__init__(self, name, hit_points, lives)
        # super(Troll, self).__init__(name, hit_points, lives)
        super().__init__(name, hit_points, lives)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print(f"****{self.name} dodges ****")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)


class TrollKing(Troll):
    def __init__(self, name="KingTroll", hit_points=140, lives=10):
        super().__init__(name)
        self.hit_points = hit_points
        self.lives = lives


    def take_damage(self, damage):
            super().take_damage(damage // 4)