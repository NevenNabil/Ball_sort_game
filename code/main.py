from game import *

if __name__ == '__main__':
    game = Game()
    print(game)
    while True:
        try:
            if game.check_game_win():
                game.win_or_except()
            stack_from = input("Select Column To Move Form :")
            stack_to = input("Select Column To Move To :")
            game.move_ball(stack_from, stack_to)
            print(game)
        except:
            game.win_or_except()
