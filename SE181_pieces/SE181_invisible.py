class Invisible():

	def __init__(self, color, number, x, y):
		
		self.color = color
		self.number = number
		self.x = x
		self.y = y
		self.P_type = "invisible"

	def __str__(self):
		return self.P_type

	def capture(self, move, board):
		
		temp = board

		for i in board:

			count = 0

			for j in i:

				if j != None and j.get_type() != "invisible":

					if j.get_number() == self.number:

						temp[i][count] = None

				count += 1

		return temp

	def get_color(self):

		return self.color

	def get_type(self):

		return self.P_type

