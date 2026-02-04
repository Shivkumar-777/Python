


# Dictionary

players = {18:"Virat" , 7:"MSD" , 45:"Rohit"}

print(players)
print(type(players))

print(players[18])    # Virat
print(players[7])     # MSD

players[7] = "Mahi"
print(players)

print(players[-2])
print(players[45])    # Rohit
print(players[1])     # Error = KeyError: 1

