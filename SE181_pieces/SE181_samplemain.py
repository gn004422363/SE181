from SE181_pawn import Pawn
from SE181_knight import Knight
from SE181_bishop import Bishop
from SE181_rook import Rook
from SE181_queen import Queen
from SE181_king import King
import termtables as tt

p1 = Pawn("Black", 1, 1, 0)
p2 = Pawn("Black", 2, 1, 1)
p3 = Pawn("Black", 3, 1, 2)
p4 = Pawn("Black", 4, 1, 3)
p5 = Pawn("Black", 5, 1, 4)
p6 = Pawn("Black", 6, 1, 5)
p7 = Pawn("Black", 7, 1, 6)
p8 = Pawn("Black", 8, 1, 7)

k1 = Knight("Black", 9, 0, 1)
k2 = Knight("Black", 10, 0, 6)

b1 = Bishop("Black", 11, 0, 2)
b2 = Bishop("Black", 12, 0, 5)

r1 = Rook("Black", 13, 0, 0)
r2 = Rook("Black", 14, 0, 7)

q1 = Queen("Black", 15, 0, 3)

king1 = King("Black", 16, 0, 4)

p9 = Pawn("White", 17, 6, 0)
p10 = Pawn("White", 18, 6, 1)
p11 = Pawn("White", 19, 6, 2)
p12 = Pawn("White", 20, 6, 3)
p13 = Pawn("White", 21, 6, 4)
p14 = Pawn("White", 22, 6, 5)
p15 = Pawn("White", 23, 6, 6)
p16 = Pawn("White", 24, 6, 7)

k3 = Knight("White", 25, 7, 1)
k4 = Knight("White", 26, 7, 6)

b3 = Bishop("White", 27, 7, 2)
b4 = Bishop("White", 28, 7, 5)

r3 = Rook("White", 29, 7, 0)
r4 = Rook("White", 30, 7, 7)

q2 = Queen("White", 31, 7, 3)

king2 = King("White", 32, 7, 4)

board = [[r1,k1,b1,q1,king1,b2,k2,r2],
         [p1,p2,p3,p4,p5,p6,p7,p8],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [None,None,None,None,None,None,None,None],
         [p9,p10,p11,p12,p13,p14,p15,p16],
         [r3,k3,b3,q2,king2,b4,k4,r4]]

def make_move(move):
    # board[move.start_x][move.start_y] = None
    board[move.end_x][move.end_y] = move.piece_move

class move():
    rows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0}
    cols = {"h":7, "g":6, "f":5, "e":4, "d":3, "c":2, "b":1, "a":0}

    def __init__(self, end, board):
        # self.start_x = start[0]
        # self.start_y = start[1]
        self.end_x = end[0]
        self.end_y = end[1]
        self.piece_move = board[self.end_x][self.end_y]
        self.piece_capture = board[self.end_x][self.end_y]


board = p4.move([3,3], True, board)

# board = q1.move([2,3], False, board)
# board = q1.move([3,3], False, board)
# board = king1.move([1,3], False, board)
# board = king1.move([0,4], False, board)
# board = king1.move([2,2], False, board)
# board = q1.move([6,7], False, board)
#
# string = tt.to_string(
#     board,
#     style=tt.styles.ascii_thin_double,
#     # alignment="ll",
#     # padding=(0, 1),
# )
#
# print(string)


