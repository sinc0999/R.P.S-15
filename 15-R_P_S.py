import os, random, pygame

"""
asigns each item a winning list, if another item is in it the first item wins
"""
os.system('cls' if os.name == 'nt' else 'clear')
class hand:

    def __init__(self, wins_against, ):
        self.wins_against = wins_against

    def check_winner(self, other_hand):
        for i in range(len(self.wins_against)):
            if self.wins_against[i] == other_hand:
                return "YOU WIN"
            else:
                return "YOU LOSE" 

rock = hand(["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"])

fire = hand(["test"])

print(rock.check_winner("fire"))