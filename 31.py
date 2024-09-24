#https://projecteuler.net/problem=31
#the number of 1p coins is unique given the number of all larger coins

combinations = 0
maximum_coins = [1,2,4,10,20,40,100,200]


for coin_200 in range(maximum_coins[0]+1):
    for coin_100 in range(maximum_coins[1]+1):
        for coin_50 in range(maximum_coins[2]+1):
            for coin_20 in range(maximum_coins[3]+1):
                for coin_10 in range(maximum_coins[4]+1):
                        for coin_5 in range(maximum_coins[5]+1):
                            for coin_2 in range(maximum_coins[6]+1):
                                if (coin_200) * 200 +(coin_100) * 100 + (coin_50) * 50 + (coin_20) * 20 + (coin_10) * 10 + (coin_5) * 5 + (coin_2) * 2  <= 200:
                                    combinations+=1
print(combinations)