import math

physics = [ 15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

class KarlPersonCoeff:
	def __init__(self, data1, data2):
		self.data1 = data1
		self.data2 = data2
	
	def get_mean(self):
		return sum( self.data1 ) / len( self.data1 ), sum( self.data2 ) / len( self.data2 )
	
	def get_cov(self):
		n1 = [i - self.get_mean()[0] for i in self.data1]
		n2 = [i - self.get_mean()[1] for i in self.data2]
		cov = [i * j for i, j in zip(n1, n2)]
		return sum( cov )

	def get_var(self):
		n1 = [ ( i - self.get_mean()[0] )**2 for i in self.data1 ]
		n2 = [ ( i - self.get_mean()[1] )**2 for i in self.data2 ]
		n1 = math.sqrt( sum( n1 ) )
		n2 = math.sqrt( sum( n2 ) )
		return n1 * n2
	
	def get_coef(self):
		return round( self.get_cov() / self.get_var(), 3 )

object = KarlPersonCoeff(physics, history)
a = object.get_coef()
print(a)
