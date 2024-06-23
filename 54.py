#problem54
#https://projecteuler.net/problem=54
def sorthand(player):
    #Input: players hand, unsorted
    #Output: players hand sorted by ascending order of the card values
    base_values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14} #assigning values to JQKA
    hand = player
    
    while True:
        changes = 0
        for i in range(3):
            if base_values[hand[i][0]] > base_values[hand[i+1][0]]:
                temp = hand[i]
                hand[i] = hand[i+1]
                hand[i+1] = temp
                changes +=1
        
        if changes == 0:
            break
    

    return hand
                

def evaluatehands(player):
    #Input: player=[a,b,c,d,e], cards are sorted by their value in an ascending order
    #Goal: Evaluate each players hand and decide 
    
    #First we will describe possible card types
    suits = {"C":"clubs","D":"diamonds","H":"hearts","S":"spades"}
    base_values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14} #assigning values to JQKA

    #We will split the cards information into two lists, first of its values and second of its suits.
    pv = [base_values[player[i][0]] for i in range(5)]
    ps = [i[1] for i in player]

    #We will define functions that will evaluate each possible combination
    def royal_flush(player_values,player_suits):

        if len({i for i in player_suits})==1 and player_values==[10,11,12,13,14]: # player has a royal flush
            return [1,[0]]
        else:
            return [0,0]
    
    def straight_flush(player_values,player_suits):

        if len({i for i in player_suits})==1 and sum(player_values)==5*(player_values[0]+player_values[4])/2: #player has a straight flush
            return [1,[max(player_values)]]
        else:
            return [0,0]
    
    def four_of_a_kind(player_values): #player has four of a kind

        if len({player_values[i] for i in range(4)})==1 or len({player_values[i+1] for i in range(4)})==1:
            return [1,[player_values[3],max([i for i in player_values if i!=player_values[3]])]]
        else:
            return [0,0]
    
    def full_house(player_values): #player has a full house

        if len({i for i in player_values})==2:
            three = player_values[0]
            for i in range(4):
                for j in range(3-i):
                    if player_values[i]==player_values[i+j+1] and player_values[i]==player_values[i+j+2]:
                        three=player_values[i]
                        break
                    else:
                        continue
                    break
            kicker = max([i for i in player_values if i!=three])


            return [1,[three,kicker]]
        else:
            return [0,0]
    
    def flush(player_values,player_suits): #player has a flush

        if len({i for i in player_suits})==1 and sum(player_values)!=5*(player_values[0]+player_values[4])/2:
            return [1,[player_values[4-i] for i in range(5)]]
        else:
            return [0,0]
        
    def straight(player_values,player_suits): #player has a straight:

        if sum(player_values)==5*(player_values[0]+player_values[4])/2 and len(set(i for i in player_suits))>1:
            return [1,[max(player_values)]]
        else:
            return [0,0]
        
    def three_of_a_kind(player_values):
        three = None
        if player_values[0]==player_values[2] or player_values[1]==player_values[3] or player_values[2]==player_values[4]:
            if len(set(i for i in player_values))==3:
                for i in range(4):
                    for j in range(3-i):
                        if player_values[i]==player_values[i+j+1] and player_values[i]==player_values[i+j+2]:
                            three=player_values[i]
                            break
                        else:
                            continue
                        break
                kicker = [i for i in player_values if i!=three]
                    
                return [1,[three,kicker[1],kicker[0]]]
            else:
                return [0,0]
        else:
            return [0,0]
    
    def two_pairs(player_values):

        if len({player_values[0],player_values[2],player_values[4]})==len({i for i in player_values}) and len({i for i in player_values})==3:
            pairs = set()
            for i in range(4):
                for j in range(4-i):
                    if player_values[i]==player_values[i+j+1]:
                        pairs.add(player_values[i])
            kicker = max([i for i in player_values if i not in pairs])
            return [1,[max(pairs),min(pairs),kicker]]
        else:
            return [0,0]
    def one_pair(player_values):

        if len({i for i in player_values})==4:
            pair = player_values[0]
            for i in range(4):
                for j in range(4-i):
                    if player_values[i]==player_values[i+j+1]:
                        pair = player_values[i]
                    break
            kicker = [i for i in player_values if i!=pair]
            return [1,[pair,kicker[2],kicker[1],kicker[0]]]
        else:
            return [0,0]
    def highest(player_values):
        if len({i for i in player_values})==5:
            return [max(player_values),[player_values[3],player_values[2],player_values[1],player_values[0]]]
        else:
            return [0,0]
    
    total = [highest(pv),one_pair(pv),two_pairs(pv),three_of_a_kind(pv),straight(pv,ps),flush(pv,ps),full_house(pv),four_of_a_kind(pv),straight_flush(pv,ps),royal_flush(pv,ps)]
    score = [total[i][0] for i in range(10)] #elements of this list are from the start: high card, one pair, two pairs, ..., straight flush, royal flush.
    extra = [total[i][1] for i in range(10)]
    return score, extra

def winner(hands):
    winning = 0
    cards = hands.split()
    player1 = [cards[i] for i in range(5)]
    player2 = [cards[i+5] for i in range(5)]
    player1 = sorthand(player1)
    player2 = sorthand(player2)

    score1, extra1 = evaluatehands(player1)
    score2, extra2 = evaluatehands(player2)
    for i in range(10):
        if score1[9-i]>score2[9-i]:
            winning = 1
            break
        elif score1[9-i]<score2[9-i]:
            winning = 2
            break
        elif score1[9-i]==1 and score2[9-i]==1:
            for j in range(len(extra1[9-i])):
                if extra1[9-i][j]<extra2[9-i][j]:
                    winning = 2
                    break
                elif extra1[9-i][j] > extra2[9-i][j]:
                    winning = 1
                    break

    return winning

victories = 0

with open('input.txt') as vstup:
    for cards in vstup:
        if winner(cards)==1:
            victories += 1

print(victories)