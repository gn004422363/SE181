from SE181_piece import piece

class Knight(piece):

	def __init__(self, color, number, x, y):

		super().__init__(color, number, x, y)
		self.P_type = "knight"

	def __str__(self):
		return self.P_type

	def validMoves(self, move, turn_1, board):

		moveList = []
		directions = [[2,-1],[2,1],[1,2],[-1,2],[-2,-1],[-2,1],[-1,-2],[1,-2]]

		for i in directions:

			temp_x = self.x + i[0]
			temp_y = self.y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			else:

				moveList.append([temp_x,temp_y])

		for i in moveList:

			if move == i:

				return True

		return False

	def attack(self, move, board):

		moveList = []
		directions = [[2,-1],[2,1],[1,2],[-1,2],[-2,-1],[-2,1],[-1,-2],[1,-2]]

		for i in directions:

			temp_x = self.x + i[0]
			temp_y = self.y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			else:

				moveList.append([temp_x,temp_y])

		for i in moveList:

			if move == i:

				return True

		return False