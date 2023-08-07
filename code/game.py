import random
import sys
from stack import *


class Game:

    def __init__(self):
        self.stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
        self.init_stacks()

    def init_stacks(self):
        balls = ["A", "B", "C", "D", "E", "A", "B", "C", "D", "E", "A", "B", "C", "D", "E", "A", "B", "C", "D", "E", ]
        random.shuffle(balls)
        self.stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
        stacks = self.stacks[0:5]
        index = 0
        for stack in stacks:
            stack.push(balls[index])
            stack.push(balls[index + 1])
            stack.push(balls[index + 2])
            stack.push(balls[index + 3])
            index += 4

    def get_busy_stack(self):
        lis = []
        for stack in self.stacks:
            if stack.getSize() > 0:
                lis.append(stack)
        return lis

    def check_game_valid(self):
        busy = self.get_busy_stack()
        if len(busy) < 7:
            return True
        tops = []
        for stack in busy:
            if stack.get_top():
                if str(stack.get_top()) in tops:
                    return True
                else:
                    tops.append(str(stack.get_top()))

        print("Game Is Not Valid Now")
        return False

    def check_game_win(self):
        busy = self.get_busy_stack()
        if len(busy) != 5:
            return False
        for stack in busy:
            values = stack.get_values()
            values = list(set(values))
            if len(values) != 1:
                return False
        print("******************* Congratulations You Win *******************")
        return True

    def move_ball(self, stack_from, stack_to):
        if stack_from not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("\nColumn Number Must Be Between 1 and 7\n")
            return False
        elif stack_to not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("\nColumn Number Must Be Between 1 and 7\n")
            return False

        stack_from = int(stack_from)
        stack_to = int(stack_to)

        if stack_from < 1 or stack_from > 7:
            print("\nColumn Number Must Be Between 1 and 7\n")
            return False
        elif stack_to < 1 or stack_to > 7:
            print("\nColumn Number Must Be Between 1 and 7\n")
            return False
        elif stack_from == stack_to:
            return False
        stack_from = stack_from - 1
        stack_to = stack_to - 1
        if self.stacks[stack_from].isEmpty():
            print("\nColumn You Want To Move From Is Empty\n")
            return False
        if self.stacks[stack_to].getSize() >= 4:
            print("\nColumn You Want To Move To Is Full\n")
            return False
        if not self.stacks[stack_to].isEmpty() and self.stacks[stack_from].get_top() != self.stacks[
            stack_to].get_top():
            print("\nThis Move Cannot Be Happened (Value Must Be The Same)\n")
            return False
        ball = self.stacks[stack_from].pop()
        self.stacks[stack_to].push(ball)
        self.move_prev_ball(stack_from, stack_to, ball)

    def move_prev_ball(self, stack_from, stack_to, ball):
        if self.stacks[stack_from].isEmpty():
            return False
        if self.stacks[stack_to].getSize() >= 4:
            return False
        if not self.stacks[stack_to].isEmpty() and self.stacks[stack_from].get_top() != self.stacks[
            stack_to].get_top():
            return False
        ball = self.stacks[stack_from].pop()
        self.stacks[stack_to].push(ball)
        self.move_prev_ball(stack_from, stack_to, ball)

    def __str__(self):
        string = ""
        for i in range(4):
            for stack in self.stacks:
                string += "  " + str(stack.get_for_print()[3 - i]) + "  "
            string += str("\n")
        string += "_____ _____ _____ _____ _____ _____ _____\n"
        string += "  1     2     3     4     5     6     7  \n"
        return string

    def win_or_except(self):
        opc = input('\nDo you want to restart or quit? (r/q): ')
        while not opc.lower() in ['r', 'q']:
            opc = input('Try again!\nDo you want to restart or quit? (r/q): ')
        if opc == 'r':
            print('Restarting the current game...\n')
            self.init_stacks()
            print(self)
        elif opc == 'q':
            sys.exit(0)
