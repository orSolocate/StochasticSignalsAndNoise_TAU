import random

# single game
def singleGame():
    toss=random.randint(1,2)
    k=1
    while toss!=1:
        toss = random.randint(1, 2)
        k=k+1
    return 2^k

def nGames(n=1):
    player1_winner_count=0
    result=[]
    for i in range(0,n):
        result.append(singleGame());
    return result;

while(True):
    n = input("Enter game number 'n' : ")
    n=int(n)
    results=nGames(n)
    p=[]
    for i in range(0,len(results)):
        number_of_2k_in_results=0
        for k in range(0,12):
            if (results[i]==2^k):
                number_of_2k_in_results=number_of_2k_in_results+1;
            p.append(number_of_2k_in_results/len(results))





