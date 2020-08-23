from SE181_piece import piece

class Pawn(piece):

	def __init__(self, color, number, x, y):

		super().__init__(color, number, x, y)
		self.P_type = "pawn"

	def __str__(self):
		return self.P_type

	def validMoves(self, move, turn_1, board):

		if self.color == "White":

			if turn_1 and move[0] == self.x - 2 and move[1] == self.y:

				return True

			elif move[0] == self.x - 1 and move[1] == self.y:

				return True

			else:

				return False

		else:

			if turn_1 and move[0] == self.x + 2 and move[1] == self.y:

				return True

			elif move[0] == self.x + 1 and move[1] == self.y:

				return True

			else:

				return False

	def attack(self, move, board):

		if self.color == "White":

			if  move[0] == self.x - 1 and (move[1] == self.y + 1 or move[1] == self.y - 1):

				return True

			else:

				return False

		else:

			if move[0] == self.x + 1 and (move[1] == self.y + 2 or move[1] == self.y - 1):

				return True

			else:

				return False