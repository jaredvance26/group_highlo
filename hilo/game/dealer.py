import random

class dealer:
    def __init__(self):
        self.points = 300
        self.card_one = None
        self.card_two = None



    def get_points(self):
        points = self.points
        card_two = self.card_two
        card_one = self.card_one
        """ This function will test if the users answer is correct (High or Low). Also will add or subtract points. """
        print(f'Points: {points}')

        question = input('[h/l]')

        if question.lower() == 'h':
        

            if card_two >= card_one:
                print()
                print(f'The card is {card_two}. + 100 points')
                points += 100
            

            elif card_two < card_one:
                print()
                print(f'The card is {card_two}. -75 points')
                points = points - 75
       

        elif question.lower() == 'l':

            if card_two <= card_one:
                print()
                print(f'The card is {card_two}. + 100 points')
                points += 100

            elif card_two > card_one:
                print()
                print(f'The card is {card_two}. -75 points.')
                points = points - 75
            
            
        else: 

            print("Enter 'h' or 'l'")
        
        print(f'Your new amount of points: {points}')
        
        self.points = points
        return self.points

    def first_card(self):
        """ Random card number generator. Pulling the card """
        self.card_one = random.randint(1,13)
        print(f'Your card is {self.card_one}')
        return self.card_one

    def second_card(self):
        """ Random card number generator. Pulling the card """
        self.card_two = random.randint(1,13)
        return self.card_two

    def test_points():
        """ This is tests if the user is able to keep playing. """

    


