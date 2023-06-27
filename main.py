from random import sample, choice
import os


CardDeck = {
    2: ['🂢', '🂲', '🃒', '🃂'],
    3: ['🂣', '🂳', '🃓', '🃃'],
    4: ['🂤', '🂴', '🃔', '🃄'],
    5: ['🂥', '🂵', '🃕', '🃅'],
    6: ['🂦', '🂶', '🃖', '🃆'],
    7: ['🂧', '🂷', '🃗', '🃇'],
    8: ['🂨', '🂸', '🃘', '🃈'],
    9: ['🂩', '🂹', '🃙', '🃉'],
    10: ['🂪', '🂺', '🃚', '🃊',
         '🂻', '🂫', '🃋', '🃛',
         '🂭', '🂽', '🃝', '🃍',
         '🃎', '🂾', '🃞', '🃎'],
    11: ['🂱', '🂡', '🃁', '🃑'],
}
DataCard = ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾',
            '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮',
            '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎',
            '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞']
tokenPlayer, tokenDealer = 0, 0
cardsPlayer, cardsDealer = '', ''


def cardShuffle(dataCard: list) -> list:
    playDeck = sample(dataCard, len(dataCard))
    for i in range(10):
        playDeck = sample(dataCard, len(dataCard))
    return playDeck


def cardSelection(dataCard: list, countCrads: int) -> list:
    resCards = [choice(dataCard) for _ in range(countCrads)]
    for card in resCards:
        dataCard.remove(card)
    return [dataCard, ' '.join(resCards)]


def countToken(playerCards: str) -> int:
    global CardDeck
    tokens = 0
    for card in playerCards.split():
        for token in CardDeck:
            if card in CardDeck[token]:
                tokens += token
                break
    return tokens


def whoWin(tokenPlayer: int, tokenDealer: int) -> str:
    return 'You Win' if tokenPlayer > tokenDealer or tokenDealer > 21 \
        else 'You Lose' if tokenPlayer < tokenDealer \
        else 'Draw'


print('Welcome to BlackJack, sir. Shall we start the game?')
messeg = input('y/n -> ')
while messeg.lower() == 'y':
    os.system('CLS')
    print("Let's start the game well.")
    print('Start or not ?')
    messeg = input('s/n -> ')
    if messeg.lower() == 's':
        os.system('CLS')
        print('---------------BLACK JACK---------------')
        deck, cardsPlayer = cardSelection(DataCard, 2)
        tokenPlayer = countToken(cardsPlayer)
        print(f'You have cards --> {cardsPlayer}')
        print(f'You have > {tokenPlayer} < tokens')
        print('\n$$$$$$$$$$$$$$$-----DEALER-----$$$$$$$$$$$$$$$')
        deck, cardsDealer = cardSelection(deck, 1)
        tokenDealer = countToken(cardsDealer)
        print(f'Dealer have --> {cardsDealer}')
        print(f'Dealer have > {tokenDealer} < tokens')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
        messeg = input('Want to take a card, continue or pass?\nt/c/p -> ')
        if messeg.lower() in 'tc':
            if messeg.lower() == 't':
                while messeg == 'yes' or messeg == 't':
                    tmp = cardSelection(deck, 1)
                    deck, cardsPlayer = tmp[0], cardsPlayer + ' ' + tmp[1]
                    tokenPlayer = countToken(cardsPlayer)
                    print(f'You have cards --> {cardsPlayer}')
                    print(f'You have > {tokenPlayer} < tokens')
                    if tokenPlayer > 21:
                        break
                    messeg = input('More?\nyes/stop -> ')
            if tokenPlayer == 21:
                print('You win')
            elif tokenPlayer > 21:
                print('You lose')
            else:
                print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                while tokenDealer < 17:
                    tmp = cardSelection(deck, 1)
                    deck, cardsDealer = tmp[0], cardsDealer + ' ' + tmp[1]
                    tokenDealer = countToken(cardsDealer)
                print(f'Dealer have --> {cardsDealer}')
                print(f'Dealer have > {tokenDealer} < tokens')
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
                print(whoWin(tokenPlayer, tokenDealer))
        else:
            print('You lose')
        messeg = input('Shall we continue the game?\ny/n -> ')
print('Until the next game, sir')
