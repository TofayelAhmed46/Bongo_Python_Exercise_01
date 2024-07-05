
def guess(a):
    guessNumber = int(input("Enter the guessing Number: "))

    if guessNumber< a:
        return "your guess is almost there."
    elif guessNumber>a:
        return 'your guess is higher.'
    else:
        return 'Your Guess Is Correct!'
    

guessingNumber = 6
print (guess(guessingNumber))