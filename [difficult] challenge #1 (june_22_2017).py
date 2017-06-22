# we all know the classic "guessing game" with higher or lower prompts.
# lets do a role reversal; you create a program that will guess numbers between 1-100,
# and respond appropriately based on whether users say that the number is too high or too low.
# Try to make a program that can guess your number based on user input and great code!

num_guesses = 0
lowest = 1
highest = 100
response = ""

while response != "y":
    guess = int((highest + lowest)/2)
    print "Is it " + str(guess) + "? If yes, type (y). If it's higher, type (h)s, if lower, type (l)"
    response = raw_input()
    if response == "y":
        print "Hooray! I guessed it in " + str(num_guesses) + " guesses"
    elif response == "h":
        lowest = guess
        num_guesses += 1
    elif response == "l":
        highest = guess
        num_guesses += 1
    else:
        print "That's not a valid response"


