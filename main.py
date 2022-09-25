import random
from hangman_art import *
from hangman_words import *
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
word = random.choice(words)
list1=[]
wrong_guesses=7
guess_entered=[]
end_game = False
lost = False
for i in range(0,len(word)):
  list1+='_'
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
print(logo)
while not end_game and not lost:
  count=0
  guess = input("Choose a letter\n").lower()
  print("\n")
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  if guess in guess_entered:
    print(f"you have already entered the letter {guess}\n")
    #if wrong_guesses<7:
      #print(hang[wrong_guesses])
    print('  '.join(list1))
    print("\n")
  else:
    for i in range(0,len(word)):
      if(word[i] == guess):
        list1[i]= guess
        count+=1
    if count==0:
      wrong_guesses-=1
      print("The letter is not in the word\n")
      print(hang[wrong_guesses])
    print('  '.join(list1))
    print("\n")
    if wrong_guesses==0:
      lost = True
      print(lost)
      print("You Lost")
    
    
    if "_" not in list1:
      end_game = True
      print("You Win")
  guess_entered+=guess