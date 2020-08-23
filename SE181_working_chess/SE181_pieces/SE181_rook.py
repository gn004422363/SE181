from SE181_piece import piece

class Rook(piece):

	def __init__(self, color, number, x, y):

		super().__init__(color, number, x, y)
		self.P_type = "rook"

	def __str__(self):
		return self.P_type

	def validMoves(self, move, turn_1, board):

		moveList = []
		directions = [[1,0],[0,1],[-1,0],[0,-1]]

		for i in directions:

			check = True
			temp_x = self.x
			temp_y = self.y

			while check:

				temp_x = temp_x + i[0]
				temp_y = temp_y + i[1]

				if temp_x < 0 or temp_y < 0:

					check = False

				elif temp_x > 7 or temp_y > 7:

					check = False

				elif board[temp_x][temp_y] != None:

					check = False

				else:

					moveList.append([temp_x,temp_y])


		for i in moveList:

			if move == i:

				return True

		return False

	def attack(self, move, board):

		moveList = []
		directions = [[1,0],[0,1],[-1,0],[0,-1]]

		for i in directions:

			check = True
			temp_x = self.x
			temp_y = self.y

			while check:

				temp_x = temp_x + i[0]
				temp_y = temp_y + i[1]

				if temp_x < 0 or temp_y < 0:

					check = False

				elif temp_x > 7 or temp_y > 7:

					check = False

				elif board[temp_x][temp_y] != None:

					moveList.append([temp_x,temp_y])
					check = False

				else:

					moveList.append([temp_x,temp_y])


		for i in moveList:

			if move == i:

				return True

		return False