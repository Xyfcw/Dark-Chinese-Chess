# coding:utf-8
from MyChess.Chess_Core import Chessman
import random




class Chessboard(object):

    def __init__(self, name):
        self.__name = name
        self.__is_red_turn = True
        self.__chessmans = [([None] * 10) for i in range(9)]
        self.__chessmans_hash = {}
        self.__history = {"red": {"chessman": None, "last_pos": None, "repeat": 0},
                          "black": {"chessman": None, "last_pos": None, "repeat": 0}}
        self.lnotdark = []
        self.ldark = []
        self.dark_to_notdark = {}

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
        red_rook_left = Chessman.Rook(" 车l红 ", "red_rook_left", True, self, False)
        self.lnotdark.append(red_rook_left)
        dark_red_rook_left = Chessman.Rook(" 暗车l红 ", "dark_red_rook_left", True, self, True)
        dark_red_rook_left.add_to_board(0, 0)
        red_rook_right = Chessman.Rook(" 车r红 ", "red_rook_right", True, self)
        self.lnotdark.append(red_rook_right)
        dark_red_rook_right = Chessman.Rook(" 暗车r红 ", "dark_red_rook_right", True, self, True)
        dark_red_rook_right.add_to_board(8, 0)
        black_rook_left = Chessman.Rook(
            " 车l黑 ", "black_rook_left", False, self)
        dark_black_rook_left = Chessman.Rook(
            " 车l黑 ", "dark_black_rook_left", False, self)
        dark_black_rook_left.add_to_board(0, 9)
        black_rook_right = Chessman.Rook(
            " 车r黑 ", "black_rook_right", False, self)
        dark_black_rook_right = Chessman.Rook(
            " 车r黑 ", "dark_black_rook_right", False, self)
        dark_black_rook_right.add_to_board(8, 9)
        red_knight_left = Chessman.Knight(
            " 马l红 ", "red_knight_left", True, self)
        red_knight_left.add_to_board(1, 0)
        red_knight_right = Chessman.Knight(
            " 马r红 ", "red_knight_right", True, self)
        red_knight_right.add_to_board(7, 0)
        black_knight_left = Chessman.Knight(
            " 马l黑 ", "black_knight_left", False, self)
        black_knight_left.add_to_board(1, 9)
        black_knight_right = Chessman.Knight(
            " 马r黑 ", "black_knight_right", False, self)
        black_knight_right.add_to_board(7, 9)
        red_cannon_left = Chessman.Cannon(
            " 炮l红 ", "red_cannon_left", True, self)
        red_cannon_left.add_to_board(1, 2)
        red_cannon_right = Chessman.Cannon(
            " 炮r红 ", "red_cannon_right", True, self)
        red_cannon_right.add_to_board(7, 2)
        black_cannon_left = Chessman.Cannon(
            " 炮l黑 ", "black_cannon_left", False, self)
        black_cannon_left.add_to_board(1, 7)
        black_cannon_right = Chessman.Cannon(
            " 炮r黑 ", "black_cannon_right", False, self)
        black_cannon_right.add_to_board(7, 7)
        red_elephant_left = Chessman.Elephant(
            " 相l红 ", "red_elephant_left", True, self)
        red_elephant_left.add_to_board(2, 0)
        red_elephant_right = Chessman.Elephant(
            " 相r红 ", "red_elephant_right", True, self)
        red_elephant_right.add_to_board(6, 0)
        black_elephant_left = Chessman.Elephant(
            " 象l黑 ", "black_elephant_left", False, self)
        black_elephant_left.add_to_board(2, 9)
        black_elephant_right = Chessman.Elephant(
            " 象r黑 ", "black_elephant_right", False, self)
        black_elephant_right.add_to_board(6, 9)
        red_mandarin_left = Chessman.Mandarin(
            " 仕l红 ", "red_mandarin_left", True, self, False)
        self.lnotdark.append(red_mandarin_left)
        dark_red_mandarin_left = Chessman.Mandarin(
            " 仕l红 ", "red_mandarin_left", True, self, True)
        dark_red_mandarin_left.add_to_board(3, 0)
        red_mandarin_right = Chessman.Mandarin(
            " 仕r红 ", "red_mandarin_right", True, self)
        red_mandarin_right.add_to_board(5, 0)
        black_mandarin_left = Chessman.Mandarin(
            " 仕l黑 ", "black_mandarin_left", False, self)
        black_mandarin_left.add_to_board(3, 9)
        black_mandarin_right = Chessman.Mandarin(
            " 仕r黑 ", "black_mandarin_right", False, self)
        black_mandarin_right.add_to_board(5, 9)
        red_king = Chessman.King(" 帅 红 ", "red_king", True, self)
        red_king.add_to_board(4, 0)
        black_king = Chessman.King(" 将 黑 ", "black_king", False, self)
        black_king.add_to_board(4, 9)
        red_pawn_1 = Chessman.Pawn(" 兵1红 ", "red_pawn_1", True, self)
        red_pawn_1.add_to_board(0, 3)
        red_pawn_2 = Chessman.Pawn(" 兵2红 ", "red_pawn_2", True, self)
        red_pawn_2.add_to_board(2, 3)
        red_pawn_3 = Chessman.Pawn(" 兵3红 ", "red_pawn_3", True, self)
        red_pawn_3.add_to_board(4, 3)
        red_pawn_4 = Chessman.Pawn(" 兵4红 ", "red_pawn_4", True, self)
        red_pawn_4.add_to_board(6, 3)
        red_pawn_5 = Chessman.Pawn(" 兵5红 ", "red_pawn_5", True, self)
        red_pawn_5.add_to_board(8, 3)
        black_pawn_1 = Chessman.Pawn(" 卒1黑 ", "black_pawn_1", False, self)
        black_pawn_1.add_to_board(0, 6)
        black_pawn_2 = Chessman.Pawn(" 卒2黑 ", "black_pawn_2", False, self)
        black_pawn_2.add_to_board(2, 6)
        black_pawn_3 = Chessman.Pawn(" 卒3黑 ", "black_pawn_3", False, self)
        black_pawn_3.add_to_board(4, 6)
        black_pawn_4 = Chessman.Pawn(" 卒4黑 ", "black_pawn_4", False, self)
        black_pawn_4.add_to_board(6, 6)
        black_pawn_5 = Chessman.Pawn(" 卒5黑 ", "black_pawn_5", False, self)
        black_pawn_5.add_to_board(8, 6)

    def disruption(self, lnotdark, ldark):
        random.shuffle(lnotdark)
        for i in range(len(ldark)):
            self.dark_to_notdark[ldark[i]] = lnotdark[i]

    def add_chessman(self, chessman, col_num, row_num):
        self.chessmans[col_num][row_num] = chessman
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

    def is_end(self):
        return self.who_is_victor(6)

    def who_is_victor(self, repeat_num):
        whos_turn = "red" if self.__is_red_turn else "black"
        other_turn = "red" if not self.__is_red_turn else "black"
        chessman = self.get_chessman_by_name("{0}_king".format(whos_turn))
        if chessman != None:
            if self.__history[other_turn]["repeat"] == repeat_num:
                print("{0} is victor".format(whos_turn))
                return True
            else:
                return False
        else:
            print("{0} is victor".format(other_turn))
            return True

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




