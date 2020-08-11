from abc import ABC, abstractmethod

class piece(ABC):

	def __init__(self, color, number, x, y):

		self.color = color
		self.number = number
		self.x = x
		self.y = y
		
	def move(self, move, turn_1, board):

		temp = board

		if 0 > move[0] > 7 or 0 > move[1] > 7:

			return True

		if board[move[0]][move[1]] != None:

			if board[move[0]][move[1]].get_color() == self.get_color():

				return board

			elif self.attack(move, board):

				temp_x = move[0]
				temp_y = move[1]
				temp[self.x][self.y], temp[move[0]][move[1]] = temp[move[0]][move[1]], temp[self.x][self.y]
				temp[self.x][self.y] = None
				self.x = temp_x
				self.y = temp_y
				return temp

			else:

				return board

		else:

			if self.validMoves(move, turn_1, board):

				temp_x = move[0]
				temp_y = move[1]
				temp[self.x][self.y], temp[move[0]][move[1]] = temp[move[0]][move[1]], temp[self.x][self.y]
				self.x = temp_x
				self.y = temp_y
				return temp

			else:

				return board

	def get_color(self):

		return self.color

	@abstractmethod
	def validMoves(self, move, turn_1):

		pass

	@abstractmethod
	def attack(self, move, board):

		pass