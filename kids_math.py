from random import randrange
class bcolors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WARN = '\033[93m'
    ENDC = '\033[0m'

def whois():
  while True:
      answer = input("Hello who are you? ")
      if answer == "Olive" or answer == "olive" :
          print ("Hello Super Olive. Get ready for some math! ")
          answer = "o"
          break
      elif answer == "Wilder" or answer == "wilder" :
          print ("Hello Super Wilder. Get ready for some math! ")
          answer = "w"
          break
      else:
          print ("This program knows about Olive and Wilder please spell your name correctly!")
  return answer

def getnumber():
  number = randrange(1,12,1)
  return number

def getpracticenum():
     while True:
          factor = input( "Now what number would you like to practice with ")
          try  :
              number = int(factor[0])
              print ("Using ", number)
              return number
              break
          except  ValueError:
              print(factor, " is not a number!")

  # if int(factor[0]):
  #     number = int(factor[0])
  #     print ("Using ", number,)
  #     return number
  #     break
  # else:
  #   print ("Be sure to enter a single number.")


def multiply(child):
    if child == "o" :
         print ("Ok Olive, we are going to practice multiplcation")
         multiplier = int(getpracticenum())
         start = 0
         goodanswers = 0
         while start < 5:
              product = int(getnumber())
              divisor = product * multiplier
              print ("What is " , divisor , " divided by " , multiplier , " ?")
              kidsanswer = int(input("Enter your answer: " ))
              correctanswer = int(divisor / multiplier)

              if kidsanswer == correctanswer:
                  print (f"{bcolors.BLUE}Hurrah!! You are correct!!{bcolors.ENDC}")
                  goodanswers += 1
              else :
                  print (f"{bcolors.WARN}Sorry. The correct answer is... {bcolors.ENDC}")
                  print (correctanswer)

              start += 1
              print ("You've got " , goodanswers , "out of 5!")
              print()
    else:
      print ("Ok Super Wilder, we are going to practice adding")
      adder = int(getpracticenum())
      start = 0
      goodanswers = 0
      while start < 5:
              randomnum = int(getnumber())
              sumnum = adder + randomnum
              print ("What is " , adder , "  plus " , randomnum , " ?")
              kidsanswer = int(input("Enter your answer: " ))
              correctanswer = int(sumnum)

              if kidsanswer == correctanswer:
                  print (f"{bcolors.BLUE}Hurrah!! You are correct!!{bcolors.ENDC}")
                  goodanswers += 1
              else :
                  print (f"{bcolors.WARN}Sorry. The correct answer is... {bcolors.ENDC}")
                  print (correctanswer)

              start += 1
              print ("You've got " , goodanswers , "out of 5!")
              print()


multiply(whois())
