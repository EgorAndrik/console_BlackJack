from random import sample
import os


class BlackJack:
    def __init__(self):
        self.CardDeck = {
            2: ['🂢', '🂲', '🃒', '🃂'],
            3: ['🂣', '🂳', '🃓', '🃃'],
            4: ['🂤', '🂴', '🃔', '🃄'],
            5: ['🂥', '🂵', '🃕', '🃅'],
            6: ['🂦', '🂶', '🃖', '🃆'],
            7: ['🂧', '🂷', '🃗', '🃇'],
            8: ['🂨', '🂸', '🃘', '🃈'],
            9: ['🂩', '🂹', '🃙', '🃉'],
            10: ['🂺', '🂻', '🂽', '🂾',
                 '🂪', '🂫', '🂭', '🂮',
                 '🃊', '🃋', '🃍', '🃎',
                 '🃚', '🃛', '🃝', '🃞'],
            11: ['🂱', '🂡', '🃁', '🃑'],
        }
        self.DataCard = [
            '🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂽', '🂾',
            '🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂭', '🂮',
            '🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃍', '🃎',
            '🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃝', '🃞'
        ]
        self.tokenPlayer, self.tokenDealer = 0, 0
        self.cardsPlayer, self.cardsDealer = '', ''
        self.cntRound, self.cntWin, self.cntLose = 0, 0, 0

    def Game(self):
        os.system('CLS')
        print('-----------------BLACK JACK------------------')
        deck = self._cardShuffle(self.DataCard)
        deck, self.cardsPlayer = self._cardSelection(deck, 2)
        self.tokenPlayer = self._countToken(self.cardsPlayer)
        print(f'You have cards --> {self.cardsPlayer}')
        print(f'You have > {self.tokenPlayer} < tokens')
        print('\n$$$$$$$$$$$$$$$-----DEALER-----$$$$$$$$$$$$$$$')
        deck, self.cardsDealer = self._cardSelection(deck, 1)
        self.tokenDealer = self._countToken(self.cardsDealer)
        print(f'Dealer have --> {self.cardsDealer}')
        print(f'Dealer have > {self.tokenDealer} < tokens')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
        messeg = input('Want to take a card, continue or pass?\nt/c/p -> ')
        if messeg.lower() in 'tc':
            if messeg.lower() == 't':
                while messeg == 'y' or messeg == 't':
                    tmp = self._cardSelection(deck, 1)
                    deck, self.cardsPlayer = tmp[0], self.cardsPlayer + ' ' + tmp[1]
                    self.tokenPlayer = self._countToken(self.cardsPlayer)
                    print(f'You have cards --> {self.cardsPlayer}')
                    print(f'You have > {self.tokenPlayer} < tokens')
                    if self.tokenPlayer > 21:
                        break
                    messeg = input('More?\ny/n -> ')
            if self.tokenPlayer == 21 and len(self.cardsPlayer.replace(' ', '')) == 2:
                print('\nYou win\n')
                self.cntWin += 1
            elif self.tokenPlayer > 21:
                print('\nYou lose\n')
                self.cntLose += 1
            else:
                print('\n$$$$$$$$$$$$$$$-----DEALER-----$$$$$$$$$$$$$$$')
                while self.tokenDealer < 17:
                    tmp = self._cardSelection(deck, 1)
                    deck, self.cardsDealer = tmp[0], self.cardsDealer + ' ' + tmp[1]
                    self.tokenDealer = self._countToken(self.cardsDealer)
                print(f'Dealer have --> {self.cardsDealer}')
                print(f'Dealer have > {self.tokenDealer} < tokens')
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                resRound = self._whoWin(self.tokenPlayer, self.tokenDealer)
                if resRound == 'You Win':
                    self.cntWin += 1
                elif resRound == 'You Lose':
                    self.cntLose += 1
                print(f'\n{resRound}\n')
        else:
            print('\nYou lose\n')
            self.cntLose += 1
        self.tokenPlayer, self.tokenDealer = '', ''
        self.tokenPlayer, self.tokenDealer = 0, 0
        self.cntRound += 1

    def getResultsGame(self):
        return f'Was {self.cntRound} rounds\nYou win {self.cntWin}\nYou lose {self.cntLose}\n'

    def _cardShuffle(self, dataCard: list) -> list:
        for i in range(42):
            dataCard = sample(dataCard, len(dataCard))
        return dataCard

    def _cardSelection(self, dataCard: list, countCrads: int) -> list:
        return [
            dataCard[countCrads:],
            ' '.join([dataCard[i] for i in range(countCrads)])
        ]

    def _countToken(self, playerCards: str) -> int:
        tokens = 0
        for card in playerCards.split():
            for token in self.CardDeck:
                if card in self.CardDeck[token]:
                    tokens += token
                    break
        return tokens

    def _whoWin(self, tokenPlayer: int, tokenDealer: int) -> str:
        return 'You Win' if tokenPlayer > tokenDealer or tokenDealer > 21 \
            else 'You Lose' if tokenPlayer < tokenDealer \
            else 'Draw'
