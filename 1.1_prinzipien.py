class Player:
    def __init__(self, name, number, position):
        self._name = name                       # Information Hiding: name is a protected attribute
        self._number = number                   # Information Hiding: number is a protected attribute
        self._position = position               # Information Hiding: position is a protected attribute
        self._goals_scored = 0                  # Information Hiding: goals_scored is a protected attribute

    # Encapsulation: describe_player and score_goal methods are part of the Player class and operate on its data
    def describe_player(self):
        print("{} wears jersey number {} and plays {}.".format(self._name, self._number, self._position))

    def score_goal(self):
        self._goals_scored += 1
        print("{} has scored a goal! Total goals scored: {}".format(self._name, self._goals_scored))

    # Polymorphismus: The __str__ method allows the Player object to be printed as a string
    def __str__(self):
        return "{} {} {} {}".format(self._name, self._position, self._number, self._goals_scored)

    # Inheritance: A subclass of Player for goalkeepers, which has an additional attribute
    def play_goalkeeper(self):
        print("{} is now playing as a goalkeeper!".format(self._name))

class Goalkeeper(Player):
    def __init__(self, name, number):
        super().__init__(name, number, "goalkeeper")
        self._saves = 0

    # Polymorphismus: The __str__ method is overridden to include the saves attribute
    def __str__(self):
        return f"{super().__str__()}, {self._saves}"
    
    def make_save(self):
        self._saves += 1
        print("{} has made a save! Total saves: {}".format(self._name, self._saves))


# Create a Player objects
player1 = Player("Lionel Messi", 10, "forward")
player2 = Player("Virgil van Dijk", 4, "defender")
player1.describe_player()                       # Output: Lionel Messi wears jersey number 10 and plays forward.
player2.describe_player()                       # Output: Virgil van Dijk wears jersey number 4 and plays defender.
player1.score_goal()                            # Output: Lionel Messi has scored a goal! Total goals scored: 1
player1.score_goal()                            # Output: Lionel Messi has scored a goal! Total goals scored: 2
player2.score_goal()                            # Output: Virgil van Dijk has scored a goal! Total goals scored: 1
print(player1)                                  # Output: Lionel Messi forward 10 2
print(player2)                                  # Output: Virgil van Dijk defender 4 1

# Create a Goalkeeper object
gk1 = Goalkeeper("Yann Sommer", 1)
gk1.describe_player()                           # Output: Yann Sommer wears jersey number 1 and plays goalkeeper.
gk1.play_goalkeeper()                           # Output: Yann Sommer is now playing as a goalkeeper!
gk1.make_save()                                 # Output: Yann Sommer has made a save! Total saves: 1
gk1.make_save()                                 # Output: Yann Sommer has made a save! Total saves: 2
print(gk1)                                      # Output: Yann Sommer goalkeeper 1 0, 2