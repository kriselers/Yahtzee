from die import Die

class Hand():
    def __init(self, dice = 5, sides = 6):
        self.dice = dice
        self.hand = []

        for _ in range(dice):
            self.hand.append(Die(None, sides))

    def all_dice(self):
        return range(1, self.dice + 1)

    def roll(self, dice):
        if [x for x in dice if x > self.dice or x < 1]:
            raise IndexError(f"You only have {self.dice} dice.")
        for i in dice:
            self.hand[i-1].roll()

    def get_hand(self):
        return [die.get_face() for die in self.hand]

    def set_faces(self, values):
        for idx, val in enumerate(values):
            self.hand[idx].set_face(val)

    def count(self, i):
        return self.get_hand().count(i)

    def sum(self):
        return sum(self.get_hand())

    def __str__(self):
        return "\n".join([f"die {idx + 1} has value {die}" for idx, die in enumerate(self.hand)])
