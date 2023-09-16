from CardGame import BlackJack


def cardGameLaunch():
    Game_BJ = BlackJack()
    print('Welcome to BlackJack, sir. Shall we start the game?')
    messeg = input('y/n -> ')
    while messeg.lower() == 'y':
        Game_BJ.Game()
        messeg = input('Shall we continue the game?\ny/n -> ')
    print('-----------------BLACK JACK------------------')
    print(Game_BJ.getResultsGame())
    print('Until the next game, sir')


if __name__ == '__main__':
    cardGameLaunch()
