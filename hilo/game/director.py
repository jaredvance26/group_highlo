from game.dealer import dealer


class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.dealer = dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
       
        self.do_updates()
        self.do_outputs()

    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.
        Args:
            self (Director): An instance of Director.
        """
        self.dealer.first_card()
        self.dealer.second_card()
        self.dealer.get_points()
        self.answer = input('Keep playing? [y/n] ')
        print(chr(27) + "[2J")

        if self.dealer.points == 0 or self.answer.lower() == 'n':
            print('Game Over')
            self.score = 0
        


    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.
        Args:
            self (Director): An instance of Director.
        """
        while self.score > 0:
            self.do_updates()

            

            