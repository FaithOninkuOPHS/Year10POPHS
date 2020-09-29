age = int(input("How old are you?"))

if age <= 11:
  print("You can watch movies rated U,PG")
elif (age >= 12) and (age <=14):
  print("You can watch movies rated U,PG,12")
elif (age <= 17) or (age ==15):
  print("You can watch movies rated U,PG,12 and 15")
elif age >= 18:
  print("You can watch all movies")
else:
  print("Enter correct age")
