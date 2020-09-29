rain =input("Is it raining ? >>").lower()
wind=input("Is it windy ? >>").lower()
if ( rain == "yes"):
  print("Take an umbrella")
elif (wind == "yes") and (rain == "yes"):
  print("It is too windy for an umbrella")
else:
  print("Enjoy your day")
    

