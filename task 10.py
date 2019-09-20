cclass rectangle():
  def __init__(self,l,b):
    self.length=l
    self.breadth=b
  def area(self):
    return self.length*self.breadth
a=int(input("Enter the dimension of length: "))
b=int(input("Enter the dimension of breadth: "))
Myrectangle=rectangle(a,b)
print("Area of the rectangle:",Myrectangle.area())
