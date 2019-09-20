a=int(input("Enter the number of elements in the list: "))
c=[]
for i in range(0,a):
  b=int(input("Enter a number : "))
  c.append(b)
print(c)
count1=0
count2=0
for num in c:
  if num%2==0:
    count1+=1
  elif num%2 != 0:
    count2+=1
print("Number of even numbers:",count1)
print("Number of odd numbers:",count2)
