class point:
    def __init__(self,  x,y):
        self.x= x
        self.y= y
    def __add__(self,other):
        x=self.x + other.x
        y=self.y +other.y
        return x,y
p1=point(3,5)
p2=point(1,2) 
print(p1+p2)

