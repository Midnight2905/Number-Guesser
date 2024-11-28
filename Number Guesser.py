#Number Guesser
import random
randNum = random.randint(0, 100)
while True:
    usrGuess = input("Guess a number: ")
    #checks to see if the user entered an int
    try:
      usrGuess = int(usrGuess)
      if(int(usrGuess) ==  randNum):
       print("You guessed correct!!!")
       quit()
      elif(int(usrGuess) < randNum):
       print("To low")
      elif(int(usrGuess) > randNum):
       print("To High")
      
    except:
      print("Please enter an int")
