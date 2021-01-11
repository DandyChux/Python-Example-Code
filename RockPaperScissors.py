import random

playerscore = 0
compscore = 0

print "First one to 10 wins!"

#pi is player input 

while (playerscore < 11) or (compscore < 11):
    pi = raw_input("Rock, Paper, Scissors? ")
    print ""
    if pi == "rock":
        comp = random.randint(1,3)
        if comp == 1:
            print "Rock. Looks like a draw."
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 2:
            print "Paper. Commputer wins."
            compscore = compscore +1
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 3:
            print "Scissors... Looks like you won."
            playerscore = playerscore + 1
            print ""
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
    
    if pi == "paper":
        comp = random.randint(1,3)
        if comp == 1:
            print "Rock. You win."
            playerscore = playerscore + 1
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 2:
            print "Paper. Looks like a draw."
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 3:
            print "Scissors! Computer wins."
            compscore = compscore + 1
            print ""
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)

    if pi == "scissors":
        comp = random.randint(1,3)
        if comp == 1:
            print "Rock. Computer wins."
            compscore = compscore + 1
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 2:
            print "Paper. Looks like you won."
            playerscore = playerscore +1
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
        elif comp == 3:
            print "Scissors! Looks like a draw."
            print ""
            print "You now have %d point(s) and the computer had %d point(s)" % (playerscore,compscore)
    
   
    







