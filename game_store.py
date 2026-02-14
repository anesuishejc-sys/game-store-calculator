# Price variables
ps3_game = 20
ps4_game = 45

#Asks for number of each game to be purchased
num_ps3_game = int(input("How many PS3 games?: "))
num_ps4_game = int(input("How many PS4 games?: "))

#Calculates total for each type of game
ps3_total = num_ps3_game * ps3_game
ps4_total = num_ps4_game * ps4_game

#Calculates total cost
total_cost = ps3_total + ps4_total

#Prints out total order cost
print("PS3 games cost: ${}\n" 
"PS4 games cost: ${}\n" 
"Total costs: ${}".format(ps3_total, ps4_total, total_cost))
