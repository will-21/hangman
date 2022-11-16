import random
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList: list) -> str:
    # Input: list
    # This function returns a random string from the passed list .

def displayBoard(missedLetters: str, correctLetters: str, secretWord: str) -> None:

def getGuess(alreadyGuessed: str) -> str:
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.

def playAgain() -> bool:
    # This function returns True if the player wants to play again; otherwise, it returns False.

def main():
	# main function

if __name__ == "__main__":
	main()
