import time
import random
dealerScore = 0
playerScore = 0
won = False ## true when score over 21

spades = [11,2,3,4,5,6,7,8,9,10,10,10,10]
clubs = [11,2,3,4,5,6,7,8,9,10,10,10,10]
diamonds= [11,2,3,4,5,6,7,8,9,10,10,10,10]
hearts = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def hit(suit):
    score = 0
    if suit == 1:
        randPlayer = random.randint(1,len(spades)-1)
        score += spades[randPlayer]
        spades.pop(randPlayer)
    if suit == 2:
        randPlayer = random.randint(1,len(clubs)-1)
        score += clubs[randPlayer]
        clubs.pop(randPlayer)
    if suit == 3:
        randPlayer = random.randint(1,len(diamonds)-1)
        score += diamonds[randPlayer]
        diamonds.pop(randPlayer)
    if suit == 4:
        randPlayer = random.randint(1,len(diamonds)-1)
        score += diamonds[randPlayer]
        diamonds.pop(randPlayer)  
    return(score)

playerScore += hit(random.randint(1,4))
dealerScore = hit(random.randint(1,4))
playerScore += hit(random.randint(1,4))
dealerHiddenCard = hit(random.randint(1,4))

while won == False:

        print("Dealer Score = " + str(dealerScore) + "\nPlayer Score = " + str(playerScore))
        time.sleep(1)
        choice = input("Do you want to hit or stand?\n")
        if choice == "hit":
            draw = hit(random.randint(1,4))
            if draw == 11 and playerScore + 11 > 21:
                draw = 1
            playerScore += draw
            if playerScore > 21:
                time.sleep(1)
                print("You lost!")
                won = True
            elif playerScore == 21:
                time.sleep(1)
                print("You won")
                won = True
        elif choice == "stand":
                time.sleep(1)
                if dealerHiddenCard == 11 and dealerScore + 11 > 21:
                     dealerHiddenCard = 1
                print("The dealers hidden card was " + str(dealerHiddenCard) + "!")
                time.sleep(1)
                dealerScore += dealerHiddenCard
                print("Their score is now " + str(dealerScore) + "!")
                while won != True:
                    if dealerScore > 21:
                        time.sleep(1)
                        print("You won!")
                        won = True
                        break
                    elif dealerScore == 21:
                        time.sleep(1)
                        print("The dealer won")
                        won = True
                        break
                    
                    draw = hit(random.randint(1,4))
                    if draw == 11 and dealerScore + 11 > 21:
                         draw = 1
                    dealerScore += draw
                    time.sleep(1)
                    print("The dealer drew " + str(draw) + "\nThe dealers score is now " + str(dealerScore))
                    time.sleep(1)