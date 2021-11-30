
class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''
    # bộ bài thực tế ko có 1 >> bỏ đi & nếu thêm 1 như đề thì khi khởi tạo sẽ ra tổ hợp 40 cặp >> dư theo y/c
    ranks = ('A', 2, 3, 4, 5, 6, 7, 8, 9)
    suits = ('♠', '♣', '♦', '♥')
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
        """
    @property
    def rank(self):
        return 1 if self._rank == 'A' else self._rank"""
    
    def __str__(self):
        '''Hiển thị lá bài'''
        i = self.rank
        j = self.suit
        return (str(self.ranks[i]) + str(self.suits[j]))

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        if self.suit > other.suit:
            return True
        elif self.suit == other.suit and self.rank > other.rank:
            return True
        else:
            return False
        