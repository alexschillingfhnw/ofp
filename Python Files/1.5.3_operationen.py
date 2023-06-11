class Player:
    def __init__(self, name, position, goals = 0):
        self.name = name
        self.position = position
        self.goals = goals

    def score_goal(self):
        self.goals += 1
        print(self.name, "scored a goal!")

player1 = Player("Mohamed Salah", "Winger", 25)
player2 = Player("Darwin Nunez", "Striker", 18)

player1.score_goal()                                # Output: Mohamed Salah scored a goal!
player2.score_goal()                                # Output: Darwin Nunez scored a goal!
player1.score_goal()                                # Output: Mohamed Salah scored a goal!

print("Salah has scored", player1.goals, "goals.")  # Output: Salah has scored 27 goals.
print("Nunez has scored", player2.goals, "goals.")  # Output: Nunez has scored 19 goals.