# Enter your code here. Read input from STDIN. Print output to STDOUT
class sy2():
    #define constructor
    def __init__(self, sx, by, bx):
        self.sx = sx
        self.by = by
        self.bx = bx

    def get_sy2(self):
        print(int(round( self.sx**2 *(self.by/ self.bx), 1)) )

obj = sy2(3, 4/5, 9/20)
obj.get_sy2()
