import random

# single game
def singleGame():
    player1=random.randint(1,36)
    player2=random.randint(1,36)
    while player1!=35 and player2!=35 or  player1==35 and player2==35:
        player1 = random.randint(1, 36)
        player2 = random.randint(1, 36)
    if player1==35:
        print ("player1 wins")
        return 1
    print ("player2 wins")
    return 2

def nGames(n=1):
    player1_winner_count=0
    for i in range(0,n):
        result=singleGame()
        if result==1:player1_winner_count+=1
    pn=(1.0*player1_winner_count)/n
    print ("probablity of player1 to win with {0} throws is {1}".format(n,pn))

while(True):
    n = raw_input("Enter game number 'n' : ")
    n=int(n)
    nGames(n)


