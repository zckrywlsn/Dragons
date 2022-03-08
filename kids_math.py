from random import randrange

def whois():
  while True:
      answer = input("Hello who are you? ")
      if answer == "Olive" or answer == "olive" :
          print ("Hello Olive. Get ready for some math! ")
          answer = "o"
          break
      elif answer == "Wilder" or answer == "wilder" :
          print ("Hellow Wilder. Get ready for some math! ")
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
          factor = input( "Now what times tables would you like to practice ")
          if int(factor[0]):
              number = int(factor[0])
              print (" Using the ", number, " times tables.")
              return number
              break
          else:
            print ("Be sure to enter a single number.")


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
                  print ("Hurrah!! You are correct!!")
                  goodanswers += 1
              else :
                  print ("The correct answer is " , correctanswer)
            
              start += 1
              print ("You got " , goodanswers , "out of 5!")
    else:
      print ("child was defined: ", child)

multiply(whois())
    
    
