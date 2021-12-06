from random import shuffle
from card import Card
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    
    def build(self):
        '''Tạo bộ bài'''
        ranks = ('A', 2, 3, 4, 5, 6, 7, 8, 9)
        suits = ('♠', '♣', '♦', '♥')
        self.cards = []
        for i in ranks:
            for j in suits:
                self.cards.append(Card(i,j))
        
    def shuffle_card(self):
        '''Trộn bài'''
        shuffle(self.cards)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if len(self.cards) > 0:
            return self.cards.pop()