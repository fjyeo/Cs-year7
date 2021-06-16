import random

random.seed()   #Prepare random number generator

print("Welcome to Freddie's number guessing game")
playagain = "yes"
guessAgain = "yes"
while playagain == "yes":
    randnum = int(random.random() * 100)
    count = 0
    while guessAgain == "yes":
        count = count + 1
        print("Guess the number")
        print(randnum)
        playerguess = int(input())
        if randnum == playerguess:
            print("Your answer is correct your number of guesses were " + str(count))
            delayCount = 0
            while delayCount < 6400:
                delayCount = delayCount + 1
            guessAgain = "No"
        else:
            delayCount = 0
            while delayCount < 8100:
                delayCount = delayCount + 1
            if playerguess > randnum:
                print("Your number is too high")
            else:
                print("your number is too low")
            if count == 1:
                print("You have had " + str(count) + " try")
            else:
                print("You have had " + str(count) + " tries")
            delayCount = 0
            while delayCount < 6400:
                delayCount = delayCount + 1
            print("Do you want to guess again ")
            guessAgain = input()
    print("Do you want to play again?")
    playagain = input()
    if playagain == "yes":
        guessAgain = "yes"
print("Thank you for playing")
