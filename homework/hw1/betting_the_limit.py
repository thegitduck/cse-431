N = 6

players = [1, 2, 3, 4, 3, 3, 2, 1]

# change string to int
for i in range(N):
    players[i] = int(players[i])

done = False
ingame = N
while ingame != 0:
  #print(ingame)
    # find minimum
    minimum = 100000
    for p in players:
        if p < minimum:
            minimum = p
    print(minimum)        
    # subtract minimum
    for i in range(N):
        if players[i] != 0:
            players[i] -= minimum
            if players[i] == 0:
                ingame -= 1
print(1)
