import random

"""

    Pick a random word from the word list
    
    Ask player to enter a letter

    Everytime the player enters a letter that is in the word, reveal that letter

    Process continues until all letters are revealed or if the player ran out of guesses

"""

wordsFile = open("Words.txt","r") #open the words file
lstWords = wordsFile.readlines() #append each word in the file onto lstWords
word = lstWords[random.randint(0,len(lstWords))] #pick a random word
word = word[:-1] #remove the newline from the word

#create the hidden word string
displayWord = ""
for letter in word:
    displayWord+="_"

deadGuyPicture = ["\nO O","\n[.]","\n---","\n | ","\n | ","\n/"," \\"] #load each part of the death picture into the deadGuyPicture list
guessCount = 0

#keep asking for input while the player has not uncovered the whole word and they have used less than 7 guesses
while displayWord != word and guessCount < 7:
    displayWordText = "Word: "

    #attach the hidden word string to the hidden word display 
    for letter in displayWord:
        displayWordText+=letter+" "

    #print the hidden word display
    print(displayWordText)

    #ask the user for a letter
    letter = input("Enter letter: ").lower()

    #if the letter is in word, edit the hidden word string to display the found letter
    if letter in word:
        for index in range(len(word)):
            if word[index]==letter:
                displayWord = displayWord[:index]+letter+displayWord[index+1:]
    else: #otherwise, increase the guesscount, and display guessCount (the amount of incorrect guesses the player used) parts of the death picture
        guessCount += 1
        for index in range(guessCount):
            print(deadGuyPicture[index],end="")
        print()

    print()

#if the guesscount is less than seven, say the player won, otherwise, say the player lossed
if guessCount < 7:

    #create a variable that stores either the singular or plural word of time to be used in the win statement depending on how many incorrect guesses the player has used.
    plural = "times"
    if guessCount == 1:
        plural = "time"
        
    print("You win! The word is {}. You guessed incorrectly {} {}.".format(displayWord,guessCount,plural))
else:
    print("You lose! The word was "+word+".")

wordsFile.close() #close the file