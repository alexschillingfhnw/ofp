class Player:
    def __init__(self, name, number, position):
        self._name = name                      
        self._number = number                   
        self._position = position             
        self._goals_scored = 0                

    def score_goal(self):
        self._goals_scored += 1
        print("{} has scored a goal! Total goals scored: {}".format(self._name, self._goals_scored))

    def __str__(self):
        return "{} {} {} {}".format(self._name, self._position, self._number, self._goals_scored)

class Goalkeeper(Player):
    def __init__(self, name, number):
        super().__init__(name, number, "goalkeeper")
        self._saves = 0

    def __str__(self):
        return "{} {}".format(super().__str__(), self._saves)
    
    def make_save(self):
        self._saves += 1
        print("{} has made a save! Total saves: {}".format(self._name, self._saves))



# Create a Player objects
player1 = Player("Lionel Messi", 10, "forward")
player2 = Player("Virgil van Dijk", 4, "defender")
player1.score_goal()                            # Output: Lionel Messi has scored a goal! Total goals scored: 1
player1.score_goal()                            # Output: Lionel Messi has scored a goal! Total goals scored: 2
player2.score_goal()                            # Output: Virgil van Dijk has scored a goal! Total goals scored: 1
print(player1)                                  # Output: Lionel Messi forward 10 2
print(player2)                                  # Output: Virgil van Dijk defender 4 1

# Create a Goalkeeper object
gk1 = Goalkeeper("Yann Sommer", 1)
gk1.make_save()                                 # Output: Yann Sommer has made a save! Total saves: 1
gk1.make_save()                                 # Output: Yann Sommer has made a save! Total saves: 2
print(gk1)                                      # Output: Yann Sommer goalkeeper 1 0, 2