class rectangle():
  def __init__(self,l,b):
    self.length=l
    self.breadth=b
  def area(self):
    return self.length*self.breadth
Myrectangle=rectangle(5,8)
print(Myrectangle.area())
