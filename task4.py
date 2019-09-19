a=input("Enter your thoughts :  ")
b=''
for i in a :
  if a.isupper()== True:
    b+=a.lower()
  elif a.islower()== True:
    b+=a.upper()
print(b)
