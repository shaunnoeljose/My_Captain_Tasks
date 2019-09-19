print("Month names= january,february,march,april,may,june,july,august,september,november,december")
month_name=str(input("Enter any month name :"))
if month_name == "february":
  print("Number of days=28 ")
elif month_name in ("april","june","september","november"):
  print("Number of days = 30 ")
elif month_name in ("january","march","may","july","august","october","december"):
  print("Number of days = 31")



