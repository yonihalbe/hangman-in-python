import random

file = open('dic.txt', 'r')
words= file.readlines()
#takes the file of all words and splits it into a list by each line


#function to generate a random word
def randomword():
    word ="aaaaaaaaaa"
    #makes sure the length of the word is not more than 8 letters
    while len(word) > 8:
        word = words[random.randint(0,len(words))]
    #picks a random word from the list
    word = word.replace("""
""", '')
    #gets rid extra line that .readlines adds
    return word
    #returns the random word as a variable to be used in the game


#function that plays the game with the random word given as an argument
def startgame(word):
    gotword = "no"
    #the number of geos user gets - length of word + 5
    goes = len(word) + 5
    print("you have ", goes, "attempts to guess the word \n")
    sofar = []
    for i in word:
        sofar.append("-")
    print (sofar, "\n")


    # lets the user guess until they run out of goes
    b = 0
    while b < goes:
        #checks if they have guessed the word by seeing if any dashes left in the
        if "-" not in sofar:
            print("well done you have guessed the word\n")
            gotword = "yes"
            break
        guess = input("guess a letter in the word: \n")
        a= 0
        success = "n"
        #uses a for loop to go thru each letter in the word to see if it matches
        #the guess and updates the list with their new letter if correct
        for i in word:
            if i == guess.lower():
                sofar[a] = i
                print('well done that letter is in the word')
                print('this is what you know so far')
                success= "y"
            a=a+1

        #checks if the letter was in word
        if success == "n":
            print("sorry that letter is not in the word pls guess again")

        #displays word so far
        print (sofar, "\n")

        #for go counter
        b = b+1
    return gotword
    

#function to check if user wants to play
def wantplay():
    choice = input("do you want to play hangman: (yes/no) ")
    if choice.lower() == "yes":
        word = randomword()
        gotword = startgame(word)
        if gotword == "no":
            print("sorry u didnt get the word")
            print("the word was ", word , "\n")
        wantplay()
    elif choice.lower() == "no":
        print ("ok see you next time")
    else:
        print("please enter a valid response \n")
        wantplay()

wantplay()
