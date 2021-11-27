from deck import Deck
from player import Player
import db
import sys


class Game:
    '''
    Class chứa các chức năng chính của game
    Game chứa danh sách người chơi, và bộ bài
    '''
    players = []
    is_deal = False
    is_flipped = False

    def __init__(self):
        pass

    def setup(self):
        print("Chào mừng đến với game đánh bài 3 cây ( vui thôi nha)")
        while True:
            try:
                number_player = int(input("Có bao nhiêu người muốn chơi: "))
                if 1 < number_player < 12:
                    for i in range(number_player):
                        self.add_player()
                    break      
                else:
                    raise ValueError ("Nhập từ 2 đến 12 người chơi")
            except ValueError:
                print("Bạn phải nhập vào số")            

    def guide(self):
        num_of_player = len(self.players)
        print('------------------------')
        print(f'1. Danh sách người chơi ({num_of_player})')
        print('2. Thêm người chơi')
        print('3. Loại người chơi')
        print('4. Chia bài')
        print('5. Lật bài')
        print('6. Xem lại game vừa chơi')
        print('7. Xem lịch sử chơi hôm nay')
        print('8. Công an tới, tốc biến :)')

        i = 0
        while(i != 8):
            try:
                i = int(input("Nhập số để chọn tính năng tương ứng: "))
                if i == 1:
                    self.list_players()
                elif i == 2:
                    self.add_player()
                elif i == 3:
                    self.remove_player()
                elif i == 4:
                    self.deal_card()
                elif i == 5:
                    self.flip_card()
                elif i == 6:
                    self.last_game()
                elif i == 7:
                    self.history()
                elif i != 8:
                    raise ValueError("Bạn cần nhập các số từ 1 đến 8")
            except BaseException as err:
                print(f"\t{err}", 'nhập lại giá trị')
        else:
            print("Đã kết thúc game")

    def list_players(self):
        print("Danh sách người chơi đang tham gia:")
        print("\tID\tName")
        i = 0
        for player in self.players:
            i += 1
            print(f"\t{i}\t{player.name}")
    
    def add_player(self):
        i = len(self.players)
        name = input(f'Tên người chơi {len(self.players) + 1}: ').strip()[0:6]
        self.players.append(Player(name))

    def remove_player(self):
        if len(self.players) ==2:
            raise ValueError("Tối thiểu phải có 2 người chơi, bạn không thể remove")
        else:
            self.list_players()
            id = int(input("Nhập ID muốn remove: "))
            self.players.pop(id-1)
            print('Đã loại người chơi thành công')
            self.list_players()

    def deal_card(self):
        '''Chia bài cho người chơi'''
        if self.is_deal:
            raise ValueError("Bài đã chia rồi, lật bài đi thôi")
        deck = Deck()
        deck.build()
        deck.shuffle_card()        
        for i in range (3):
            for player in self.players:
                player.add_card(deck.deal_card())
        self.is_deal = True  
        print("Bài đã chia xong, xuống tiền nào")      
        
        '''
        if self.is_deal:
            raise ValueError("Bài đã chia rồi, lật bài đi thôi")
        deck = Deck()
        deck.build()
        deck.shuffle_card()        
        for i in range (3):
            for player in self.players:
                card = self.deck.deal_card()
                player.add_card(card)
        self.is_deal = True  
        print("Bài đã chia xong, xuống tiền nào")   '''
        
        '''''''''
        if self.is_dealt:
            raise error.DealtError()
        else:
            for player in self.players:
                player.remove_cards()

            self.deck.build()
            self.deck.shuffle_cards()

            for i in range(Game.cards_per_player):
                for player in self.players:
                    card = self.deck.deal_card()
                    player.add_card(card)

            self.is_dealt = True
            self.is_flipped = False
            self.is_playing = True

            print('Bài đã chia :)\nXuống tiền đi nào')'''

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        if not self.is_deal:
            raise ValueError("Chưa chia bài bạn ơi, chia đã rồi mới lật được nhé")
        for player in self.players:
            print (f"Người chơi {player.name}", end=": ")
            print(player.flip_card(), end="")
            print (f", Tổng điểm {player.point}, lá bài lớn nhất {player.biggest_card}")
        
        win = max(self.players)
        print(f"Chúc mừng {win.name} đã có tiền") 
        db.log(win, self.players)

        self.is_deal = False
        for player in self.players:
            player.remove_card()
            
    def last_game(self):
        game, logs = db.get_last_game()
        if game is not None:
            print ("Thời gian: ", game['play_at'], ' Người chiến thắng: ', game['winner'])
            for log in logs:
                print (f"Người chơi {log['player']}: {log['cards']}", end="")                
                print (f", Tổng điểm {log['point']}, lá bài lớn nhất {log['biggest_card']}")       

    def history(self):
        historys = db.history()
        list_str = ""
        count_all = 0
        if historys is not None:
            for history in historys:
               count_all += history['count']
               list_str += f"\t{history['winner']} \tthắng {history['count']} ván\n"   
        print (f"Tổng số ván đã chơi: {count_all} ván")     
        print (list_str)  