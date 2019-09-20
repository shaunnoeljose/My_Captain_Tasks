def mult(x):
  count=1
  for i in x:
    count=count*i
  return count
a=int(input("Enter the number of elements in the list: "))
c=[]
for i in range(0,a):
  b=int(input("Enter the value : "))
  c.append(b)
print(mult(c))
