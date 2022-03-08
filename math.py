
def whois():
  while True:
      answer = input("Hello who are you? ")
      if answer == "Olive" or answer == "olive" :
          print ("Hello Olive. Get ready for some math! ")
          break
      elif answer == "Wilder" or answer == "wilder" :
          print ("Hellow Wilder. Get ready for some math! ")
          break
      else:
          print ("This program knows about Olive and Wilder please spell your name correctly!")
whois()
