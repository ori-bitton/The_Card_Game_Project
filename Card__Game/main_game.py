from Card__Game.Loading import Loading
from Card__Game.DeckOfCards import DeckOfCards
from Card__Game.CardGame import CardGame
from pyfiglet import Figlet

deck = DeckOfCards()
game = CardGame('Player 1', 'Player 2', deck)

custom_fig = Figlet(font='ivrit')
print(custom_fig.renderText('מלחמה'))


print("Players:")
game.player1.show()
game.player2.show()
load = Loading(5)

print("\nStart Game !")
for i in range(10):
    load = Loading(3)
    player1_card = game.player1.get_card()
    player2_card = game.player2.get_card()
    if player1_card > player2_card:
        game.player2.add_card(player1_card)
        game.player2.add_card(player2_card)
        print(f"Round {i+1} Winner: {game.player1.name} ({len(game.player1.playerdeck)} Cards)")
        print(f"Cards thrown: {player1_card}, {player2_card}.")
    elif player2_card > player1_card:
        game.player1.add_card(player1_card)
        game.player1.add_card(player2_card)
        print(f"Round {i + 1} Winner: {game.player2.name} ({len(game.player2.playerdeck)} Cards)")
        print(f"Cards thrown: {player1_card}, {player2_card}.")

load = Loading(2)
winner = game.get_winner()
if winner is None:
    print("Game Draw")
    game.player1.show()
    game.player2.show()
else:
    print(f"Game Winner: ")
    winner.show()
