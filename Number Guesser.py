#Number Guesser
import random
randNum = random.randint(0, 999)
while True:
    usrGuess = input("Guess a number: ")
    if(int(usrGuess) > randNum):
     print("To high")
    if(int(usrGuess) < randNum):
     print("To low")
    if(int(usrGuess) == randNum):
      print("You guessed correct!!!")
      quit()
    