from SE181_piece import piece

class King(piece):

	def __init__(self, color, number, x, y):

		super().__init__(color, number, x, y)
		self.P_type = "king"

	def __str__(self):
		return self.P_type

	def validMoves(self, move, turn_1, board):

		moveList = []
		directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

		for i in directions:

			temp_x = self.x
			temp_y = self.y

			temp_x = temp_x + i[0]
			temp_y = temp_y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			elif board[temp_x][temp_y] != None:

				pass

			else:

				moveList.append([temp_x,temp_y])


		for i in moveList:

			if move == i:

				return True

		return False

	def attack(self, move, board):

		moveList = []
		directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

		for i in directions:

			check = True
			temp_x = self.x
			temp_y = self.y

			temp_x = temp_x + i[0]
			temp_y = temp_y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			elif board[temp_x][temp_y] != None:

				moveList.append([temp_x,temp_y])

			else:

				pass


		for i in moveList:

			if move == i:

				return True

		return False
	def castleKingside(self, move, turn1, board):

		moveList = []
		directions = [[0,2]]

		for i in directions:

			check = True
			temp_x = self.x
			temp_y = self.y

			temp_x = temp_x + i[0]
			temp_y = temp_y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			elif board[temp_x][temp_y] != None:

				pass

			elif board[temp_x-1][temp_y-1] != None:

				pass

			elif turn_1:

				moveList.append([temp_x,temp_y])
			else:
				pass


		for i in moveList:

			if move == i:

				return True

		return False
	def castleQueenside(self, move, turn1, board):

		moveList = []
		directions = [[0,-2]]

		for i in directions:

			check = True
			temp_x = self.x
			temp_y = self.y

			temp_x = temp_x + i[0]
			temp_y = temp_y + i[1]

			if temp_x < 0 or temp_y < 0:

				pass

			elif temp_x > 7 or temp_y > 7:

				pass

			elif board[temp_x][temp_y] != None:

				pass

			elif board[temp_x+1][temp_y+1] != None:

				pass

			elif board[temp_x+2][temp_y+2] != None:

				pass

			elif turn_1:

				moveList.append([temp_x,temp_y])
			else:
				pass


		for i in moveList:

			if move == i:

				return True

		return False
