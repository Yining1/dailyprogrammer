# https://www.reddit.com/r/dailyprogrammer/comments/pkwgf/2112012_challenge_3_difficult/
# Welcome to cipher day!
# For this challenge, you need to write a program that will take the scrambled words from this post
# (https://pastebin.com/jSD873gL), and compare them against THIS WORD LIST to unscramble them.
# For bonus points, sort the words by length when you are finished.
# Post your programs and/or subroutines!
# Here are your words to de-scramble:
# mkeart
# sleewa
# edcudls
# iragoge
# usrlsle
# nalraoci
# nsdeuto
# amrhat
# inknsy
# iferkna

from urllib import urlopen

to_descramble = {"mkeart", "sleewa", "edcudls", "iragoge", "usrlsle",
                 "nalraoci", "nsdeuto", "amrhat", "inknsy", "iferkna"}
word_list = urlopen("https://pastebin.com/jSD873gL").read().split()

answers = []

for word in word_list:
    for scrambled in to_descramble:
        if sorted(word) == sorted(scrambled):
            answers.append(word)

print sorted(answers, key=len)