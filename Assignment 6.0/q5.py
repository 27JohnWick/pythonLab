tRecords = {}
while True:
    tName = input("Enter a team name: ")
    if not tName:
        break
    wins = int(input("Enter the number of wins: "))
    losses = int(input("Enter the number of losses: "))
    tRecords[tName] = [wins, losses]
tName = input("Enter a team name: ")
winPercentage = tRecords[tName][0] / sum(tRecords[tName])
print(winPercentage)
wins_list = [team[0] for team in tRecords.values()]
winTeam = [team for team, record in tRecords.items() if record[0] > record[1]]
print(winTeam)
