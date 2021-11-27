from logging import error, raiseExceptions
from game import Game

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    
    game = Game()
    game.setup()
    game.guide()

if __name__ == '__main__':
    main()
