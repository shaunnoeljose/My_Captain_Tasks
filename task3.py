a=[]
c=int(input("Enter the number of words in the list: "))
for i in range(0,c):
  word=str(input("Enter the word: "))
  a.append(word)
print(a)
count=len(a[0])
longest_word=a[0]
for i in a:
  if len(i)>count:
   longest_word=i
print(longest_word)
