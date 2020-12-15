# coding:utf-8
import pygame
from MyChess.Chess_Core import Chessman
import random
from enum import Enum

from pygame.rect import Rect

Winner = Enum("Winner", "red black draw")

class Chessboard(object):

    def __init__(self, name):
        self.__name = name
        self.__is_red_turn = True
        self.__chessmans = [([None] * 10) for i in range(9)]
        self.__chessmans_hash = {}
        self.__history = {"red": {"chessman": None, "last_pos": None, "repeat": 0},
                          "black": {"chessman": None, "last_pos": None, "repeat": 0}}
        self.winner = None
        self.list_red_bright = []
        self.list_red_dark = []
        self.list_black_bright = []
        self.list_black_dark = []
        self.d_to_b = {}

    @property
    def is_red_turn(self):
        return self.__is_red_turn

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def chessmans(self):
        return self.__chessmans

    @property
    def chessmans_hash(self):
        return self.__chessmans_hash

    def init_board(self):
        dark_red_rook_left = Chessman.Rook(
            " 暗车l红 ", "dark_red_rook_left", True, self, True)
        dark_red_rook_left.add_to_board(0, 0)
        dark_red_rook_right = Chessman.Rook(
            " 暗车r红 ", "dark_red_rook_right", True, self, True)
        dark_red_rook_right.add_to_board(8, 0)
        dark_black_rook_left = Chessman.Rook(
            " 暗车l黑 ", "dark_black_rook_left", False, self, True)
        dark_black_rook_left.add_to_board(0, 9)
        dark_black_rook_right = Chessman.Rook(
            " 暗车r黑 ", "dark_black_rook_right", False, self, True)
        dark_black_rook_right.add_to_board(8, 9)
        dark_red_knight_left = Chessman.Knight(
            " 暗马l红 ", "dark_red_knight_left", True, self, True)
        dark_red_knight_left.add_to_board(1, 0)
        dark_red_knight_right = Chessman.Knight(
            " 暗马r红 ", "dark_red_knight_right", True, self, True)
        dark_red_knight_right.add_to_board(7, 0)
        dark_black_knight_left = Chessman.Knight(
            " 暗马l黑 ", "dark_black_knight_left", False, self, True)
        dark_black_knight_left.add_to_board(1, 9)
        dark_black_knight_right = Chessman.Knight(
            " 暗马r黑 ", "dark_black_knight_right", False, self, True)
        dark_black_knight_right.add_to_board(7, 9)
        dark_red_cannon_left = Chessman.Cannon(
            " 暗炮l红 ", "dark_red_cannon_left", True, self, True)
        dark_red_cannon_left.add_to_board(1, 2)
        dark_red_cannon_right = Chessman.Cannon(
            " 暗炮r红 ", "dark_red_cannon_right", True, self, True)
        dark_red_cannon_right.add_to_board(7, 2)
        dark_black_cannon_left = Chessman.Cannon(
            " 暗炮l黑 ", "dark_black_cannon_left", False, self, True)
        dark_black_cannon_left.add_to_board(1, 7)
        dark_black_cannon_right = Chessman.Cannon(
            " 暗炮r黑 ", "dark_black_cannon_right", False, self, True)
        dark_black_cannon_right.add_to_board(7, 7)
        dark_red_elephant_left = Chessman.Elephant(
            " 暗相l红 ", "dark_red_elephant_left", True, self, True)
        dark_red_elephant_left.add_to_board(2, 0)
        dark_red_elephant_right = Chessman.Elephant(
            " 暗相r红 ", "dark_red_elephant_right", True, self, True)
        dark_red_elephant_right.add_to_board(6, 0)
        dark_black_elephant_left = Chessman.Elephant(
            " 暗象l黑 ", "dark_black_elephant_left", False, self, True)
        dark_black_elephant_left.add_to_board(2, 9)
        dark_black_elephant_right = Chessman.Elephant(
            " 暗象r黑 ", "dark_black_elephant_right", False, self, True)
        dark_black_elephant_right.add_to_board(6, 9)
        dark_red_mandarin_left = Chessman.Mandarin(
            " 暗仕l红 ", "dark_red_mandarin_left", True, self, True)
        dark_red_mandarin_left.add_to_board(3, 0)
        dark_red_mandarin_right = Chessman.Mandarin(
            " 暗仕r红 ", "dark_red_mandarin_right", True, self, True)
        dark_red_mandarin_right.add_to_board(5, 0)
        dark_black_mandarin_left = Chessman.Mandarin(
            " 暗仕l黑 ", "dark_black_mandarin_left", False, self, True)
        dark_black_mandarin_left.add_to_board(3, 9)
        dark_black_mandarin_right = Chessman.Mandarin(
            " 暗仕r黑 ", "dark_black_mandarin_right", False, self, True)
        dark_black_mandarin_right.add_to_board(5, 9)
        red_king = Chessman.King(" 帅 红 ", "red_king", True, self)
        red_king.add_to_board(4, 0)
        black_king = Chessman.King(" 将 黑 ", "black_king", False, self)
        black_king.add_to_board(4, 9)
        dark_red_pawn_1 = Chessman.Pawn(" 暗兵1红 ", "dark_red_pawn_1", True, self, True)
        dark_red_pawn_1.add_to_board(0, 3)
        dark_red_pawn_2 = Chessman.Pawn(" 暗兵2红 ", "dark_red_pawn_2", True, self, True)
        dark_red_pawn_2.add_to_board(2, 3)
        dark_red_pawn_3 = Chessman.Pawn(" 暗兵3红 ", "dark_red_pawn_3", True, self, True)
        dark_red_pawn_3.add_to_board(4, 3)
        dark_red_pawn_4 = Chessman.Pawn(" 暗兵4红 ", "dark_red_pawn_4", True, self, True)
        dark_red_pawn_4.add_to_board(6, 3)
        dark_red_pawn_5 = Chessman.Pawn(" 暗兵5红 ", "dark_red_pawn_5", True, self, True)
        dark_red_pawn_5.add_to_board(8, 3)
        dark_black_pawn_1 = Chessman.Pawn(" 暗卒1黑 ", "dark_black_pawn_1", False, self, True)
        dark_black_pawn_1.add_to_board(0, 6)
        dark_black_pawn_2 = Chessman.Pawn(" 暗卒2黑 ", "dark_black_pawn_2", False, self, True)
        dark_black_pawn_2.add_to_board(2, 6)
        dark_black_pawn_3 = Chessman.Pawn(" 暗卒3黑 ", "dark_black_pawn_3", False, self, True)
        dark_black_pawn_3.add_to_board(4, 6)
        dark_black_pawn_4 = Chessman.Pawn(" 暗卒4黑 ", "dark_black_pawn_4", False, self, True)
        dark_black_pawn_4.add_to_board(6, 6)
        dark_black_pawn_5 = Chessman.Pawn(" 暗卒5黑 ", "dark_black_pawn_5", False, self, True)
        dark_black_pawn_5.add_to_board(8, 6)



    def get_bright_chessman(self):
        red_rook_left = Chessman.Rook(" 车l红 ", "red_rook_left", True, self)
        self.list_red_bright.append(red_rook_left)

        red_rook_right = Chessman.Rook(" 车r红 ", "red_rook_right", True, self)
        self.list_red_bright.append(red_rook_right)

        black_rook_left = Chessman.Rook(
            " 车l黑 ", "black_rook_left", False, self)
        self.list_black_bright.append(black_rook_left)

        black_rook_right = Chessman.Rook(
            " 车r黑 ", "black_rook_right", False, self)
        self.list_black_bright.append(black_rook_right)

        red_knight_left = Chessman.Knight(
            " 马l红 ", "red_knight_left", True, self)
        self.list_red_bright.append(red_knight_left)

        red_knight_right = Chessman.Knight(
            " 马r红 ", "red_knight_right", True, self)
        self.list_red_bright.append(red_knight_right)

        black_knight_left = Chessman.Knight(
            " 马l黑 ", "black_knight_left", False, self)
        self.list_black_bright.append(black_knight_left)

        black_knight_right = Chessman.Knight(
            " 马r黑 ", "black_knight_right", False, self)
        self.list_black_bright.append(black_knight_right)

        red_cannon_left = Chessman.Cannon(
            " 炮l红 ", "red_cannon_left", True, self)
        self.list_red_bright.append(red_cannon_left)

        red_cannon_right = Chessman.Cannon(
            " 炮r红 ", "red_cannon_right", True, self)
        self.list_red_bright.append(red_cannon_right)

        black_cannon_left = Chessman.Cannon(
            " 炮l黑 ", "black_cannon_left", False, self)
        self.list_black_bright.append(black_cannon_left)

        black_cannon_right = Chessman.Cannon(
            " 炮r黑 ", "black_cannon_right", False, self)
        self.list_black_bright.append(black_cannon_right)

        red_elephant_left = Chessman.Elephant(
            " 相l红 ", "red_elephant_left", True, self)
        self.list_red_bright.append(red_elephant_left)

        red_elephant_right = Chessman.Elephant(
            " 相r红 ", "red_elephant_right", True, self)
        self.list_red_bright.append(red_elephant_right)

        black_elephant_left = Chessman.Elephant(
            " 象l黑 ", "black_elephant_left", False, self)
        self.list_black_bright.append(black_elephant_left)

        black_elephant_right = Chessman.Elephant(
            " 象r黑 ", "black_elephant_right", False, self)
        self.list_black_bright.append(black_elephant_right)

        red_mandarin_left = Chessman.Mandarin(
            " 仕l红 ", "red_mandarin_left", True, self)
        self.list_red_bright.append(red_mandarin_left)

        red_mandarin_right = Chessman.Mandarin(
            " 仕r红 ", "red_mandarin_right", True, self)
        self.list_red_bright.append(red_mandarin_right)

        black_mandarin_left = Chessman.Mandarin(
            " 仕l黑 ", "black_mandarin_left", False, self)
        self.list_black_bright.append(black_mandarin_left)

        black_mandarin_right = Chessman.Mandarin(
            " 仕r黑 ", "black_mandarin_right", False, self)
        self.list_black_bright.append(black_mandarin_right)

        red_pawn_1 = Chessman.Pawn(" 兵1红 ", "red_pawn_1", True, self)
        self.list_red_bright.append(red_pawn_1)

        red_pawn_2 = Chessman.Pawn(" 兵2红 ", "red_pawn_2", True, self)
        self.list_red_bright.append(red_pawn_2)

        red_pawn_3 = Chessman.Pawn(" 兵3红 ", "red_pawn_3", True, self)
        self.list_red_bright.append(red_pawn_3)

        red_pawn_4 = Chessman.Pawn(" 兵4红 ", "red_pawn_4", True, self)
        self.list_red_bright.append(red_pawn_4)

        red_pawn_5 = Chessman.Pawn(" 兵5红 ", "red_pawn_5", True, self)
        self.list_red_bright.append(red_pawn_5)

        black_pawn_1 = Chessman.Pawn(" 卒1黑 ", "black_pawn_1", False, self)
        self.list_black_bright.append(black_pawn_1)

        black_pawn_2 = Chessman.Pawn(" 卒2黑 ", "black_pawn_2", False, self)
        self.list_black_bright.append(black_pawn_2)

        black_pawn_3 = Chessman.Pawn(" 卒3黑 ", "black_pawn_3", False, self)
        self.list_black_bright.append(black_pawn_3)

        black_pawn_4 = Chessman.Pawn(" 卒4黑 ", "black_pawn_4", False, self)
        self.list_black_bright.append(black_pawn_4)

        black_pawn_5 = Chessman.Pawn(" 卒5黑 ", "black_pawn_5", False, self)
        self.list_black_bright.append(black_pawn_5)

        self.dark_to_bright(self.list_red_dark, self.list_red_bright,
                            self.list_black_dark, self.list_black_bright)


    def dark_to_bright(self, rd, rb, bd, bb):
        # print(len(rd),len(rb),len(bd),len(bb))
        random.shuffle(rb)
        random.shuffle(bb)
        for i in range(15):
            self.d_to_b[rd[i]] = rb[i]
            self.d_to_b[bd[i]] = bb[i]

    # def draw_dead_chessman(self, chessman):
    #     ball = pygame.image.load('ball.png')  # 加载图片
    #     screen.

    def add_chessman(self, chessman, col_num, row_num):
        self.chessmans[col_num][row_num] = chessman
        if chessman.is_dark:
            if chessman.is_red:
                self.list_red_dark.append(chessman)
            else:
                self.list_black_dark.append(chessman)
        if chessman.name not in self.__chessmans_hash:
            self.__chessmans_hash[chessman.name] = chessman

    def remove_chessman_target(self, col_num, row_num):
        chessman_old = self.get_chessman(col_num, row_num)
        if chessman_old != None:
            self.__chessmans_hash.pop(chessman_old.name)

    def remove_chessman_source(self, col_num, row_num):
        self.chessmans[col_num][row_num] = None

    def calc_chessmans_moving_list(self):
        for chessman in self.__chessmans_hash.values():
            if chessman.is_red == self.__is_red_turn:
                chessman.calc_moving_list()

    def clear_chessmans_moving_list(self):
        for chessman in self.__chessmans_hash.values():
            chessman.clear_moving_list()

    def move_chessman(self, chessman, col_num, row_num):
        if chessman.is_red == self.__is_red_turn:
            # self.remove_chessman_source(chessman.col_num, chessman.row_num)
            self.remove_chessman_target(col_num, row_num)
            self.add_chessman(chessman, col_num, row_num)
            self.__is_red_turn = not self.__is_red_turn
            return True
        else:
            print("the wrong turn")
            return False

    def update_history(self, chessman, col_num, row_num):
        red_or_black = self.red_or_black(chessman)
        history_chessman = self.__history[red_or_black]["chessman"]
        history_pos = self.__history[red_or_black]["last_pos"]
        if history_chessman == chessman and history_pos != None and history_pos[0] == col_num and history_pos[1] == row_num:
            self.__history[red_or_black]["repeat"] += 1
        else:
            self.__history[red_or_black]["repeat"] = 0
        self.__history[red_or_black]["chessman"] = chessman
        self.__history[red_or_black]["last_pos"] = (
            chessman.col_num, chessman.row_num)

    def red_or_black(self, chessman):
        if chessman.is_red:
            return "red"
        else:
            return "black"

    def move_to_str(self, x0, y0, x1, y1):
        return str(x0) + str(y0) + str(x1) + str(y1)

    def legal_moves(self):

        # return all legal moves

        _legal_moves = []
        for chessman in self.__chessmans_hash.values():
            if chessman.is_red == self.is_red_turn:
                p = chessman.position
                x0 = p.x
                y0 = p.y
                for point in chessman.moving_list:
                    _legal_moves.append(self.move_to_str(x0, y0, point.x, point.y))
        return _legal_moves

    def avoid_dui_jiang(self, chessman, col_num, row_num):
        red_king = self.get_chessman_by_name('red_king')
        black_king = self.get_chessman_by_name('black_king')
        if type(chessman) != type(red_king):
            if red_king.position.x == black_king.position.x == chessman.position.x:
                num = 0
                for i in range(red_king.position.y + 1, black_king.position.y):
                    if self.chessmans[red_king.position.x][i] != None:
                        num += 1
                if num == 1:
                    t = chessman.moving_list.copy()
                    for point in t:
                        if point.x != chessman.position.x:
                            chessman.moving_list.remove(point)
        elif chessman == red_king:
            checking = True
            if col_num == black_king.position.x:
                for i in range(row_num + 1, black_king.position.y):
                    if self.chessmans[red_king.position.x][i] != None:
                        checking = False
                        break
                if checking:
                    for point in chessman.moving_list:
                        if point.x == col_num and point.y == row_num:
                            chessman.moving_list.remove(point)
                            break
        else:
            checking = True
            if col_num == red_king.position.x:
                for i in range(red_king.position.x + 1, row_num):
                    if self.chessmans[red_king.position.x][i] != None:
                        checking = False
                        break
                if checking:
                    for point in chessman.moving_list:
                        if point.x == col_num and point.y == row_num:
                            chessman.moving_list.remove(point)
                            break

    def is_end(self, count):
        red_king = self.get_chessman_by_name('red_king')
        black_king = self.get_chessman_by_name('black_king')
        # if not red_king:
        #     self.winner = Winner.black
        # elif not black_king:
        #     self.winner = Winner.red
        if count == 40:
            print('it ends in a draw')
            return True # 游戏结束，平局
        # elif red_king.position.x == black_king.position.x:
        #     checking = True
        #     for i in range(red_king.position.y + 1, black_king.position.y):
        #         if self.chessmans[red_king.position.x][i] != None:
        #             checking = False
        #             break
        #
        #     if checking: # 如果对将
        #         if self.is_red_turn:
        #             self.winner = Winner.red
        #         else:
        #             self.winner = Winner.black
        # if self.winner is None:
        else:
            legal_moves = self.legal_moves()
            if legal_moves == []:
                if self.is_red_turn:
                    self.winner = Winner.black
                else:
                    self.winner = Winner.red
            elif self.is_red_turn:
                target = black_king.position
            else:
                target = red_king.position
            for move in legal_moves:
                if int(move[2]) == target.x and int(move[3]) == target.y:
                    if self.is_red_turn:
                        self.winner = Winner.red
                    else:
                        self.winner = Winner.black
                    print(target.x, target.y)
                    break
        if self.winner:
            print("{0} is victor".format(self.winner))
            # print(flag)
        return self.winner != None

    # def is_end(self):
    #     return self.who_is_victor(6)
    #
    # def who_is_victor(self, repeat_num):
    #     whos_turn = "red" if self.__is_red_turn else "black"
    #     other_turn = "red" if not self.__is_red_turn else "black"
    #     chessman = self.get_chessman_by_name("{0}_king".format(whos_turn))
    #     if chessman != None:
    #         if self.__history[other_turn]["repeat"] == repeat_num:
    #             print("{0} is victor".format(whos_turn))
    #             return True
    #         else:
    #             return False
    #     else:
    #         print("{0} is victor".format(other_turn))
    #         return True


    def get_chessman(self, col_num, row_num):
        return self.__chessmans[col_num][row_num]

    def get_chessman_by_name(self, name):
        if name in self.__chessmans_hash:
            return self.__chessmans_hash[name]

    def get_top_first_chessman(self, col_num, row_num):
        for i in range(row_num + 1, 10, 1):
            current = self.chessmans[col_num][i]
            if current != None:
                return current

    def get_bottom_first_chessman(self, col_num, row_num):
        for i in range(row_num - 1, -1, -1):
            current = self.chessmans[col_num][i]
            if current != None:
                return current

    def get_left_first_chessman(self, col_num, row_num):
        for i in range(col_num - 1, -1, -1):
            current = self.chessmans[i][row_num]
            if current != None:
                return current

    def get_right_first_chessman(self, col_num, row_num):
        for i in range(col_num + 1, 9, 1):
            current = self.chessmans[i][row_num]
            if current != None:
                return current

    def get_top_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(row_num + 1, 10, 1):
            current = self.chessmans[col_num][i]
            if current != None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_bottom_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(row_num - 1, -1, -1):
            current = self.chessmans[col_num][i]
            if current != None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_left_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(col_num - 1, -1, -1):
            current = self.chessmans[i][row_num]
            if current != None:
                if count == 1:
                    return current
                else:
                    count += 1

    def get_right_second_chessman(self, col_num, row_num):
        count = 0
        for i in range(col_num + 1, 9, 1):
            current = self.chessmans[i][row_num]
            if current != None:
                if count == 1:
                    return current
                else:
                    count += 1

    def print_to_cl(self):
        screen = "\r\n"
        for i in range(9, -1, -1):
            for j in range(9):
                if self.__chessmans[j][i] != None:
                    screen += self.__chessmans[j][i].name_cn
                else:
                    screen += "   .   "
            screen += "\r\n" * 3
        print(screen)




