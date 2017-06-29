# Arrr, me mateys! Yer' challenge fer' today be a tough one. It be gettin awfully borein' on the high seas, so yer' job
# be to create a pirate based fightin' game! This game oughter' be turn based, and you oughter' be able to pick yer
# attacks every turn. The best game'll be winnin' some custom flair, and all the rest o' ya will be walkin the plank!

# this pirate is having a very bad day

response = ""

fightingDialogue = [
    "A seagull swoops down! Will you <attack> or <flee>?",
    "A friend says hello, will you <attack> or <flee>?",
    "Some rain falls on your face! Will you <attack> the water or <flee>?",
    "You trip on a rock! Will you <attack> or <flee>?"
]



while response != "quit":
    print "Type <quit> to quit"
    for dialogue in fightingDialogue:
        print dialogue
        response = str(raw_input())
        if response == "quit":
            break



