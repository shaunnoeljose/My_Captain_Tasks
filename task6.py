a=float(input("Enter the 1st side of the triangle: "))
b=float(input("Enter the 2nd side of the triangle: "))
c=float(input("Enter the 3rd side of the triangle: "))
if a==b and b==c :
  print("The triangle is equilateral")
elif a!=b and b!=c :
  print("The triangle is scalene")
elif a==b and b!=c or b==c and c!=a:
  print("The triangle is isosceles")
