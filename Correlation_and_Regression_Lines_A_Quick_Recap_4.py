
class getx():
    def __init__(self, Xcoef, Ycoef, const, Yval):
        self.Xcoef = Xcoef
        self.Ycoef = Ycoef
        self.const = const
        self.Yval = Yval

    def get_value(self):
        print( round( (self.const + self.Ycoef * self.Yval) / self.Xcoef, 1) ) 


obj = getx(20, 9, 107, 7)
obj.get_value()
