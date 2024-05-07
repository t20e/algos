competitions = [
    ['html', "c#"],
    ['c#', "Python"],
    ['Python', 'html'],
]
results = [0, 0, 1]
def tournamentWinner(competitions, results):
    teams = {}
    for i in competitions:
        for t in i:
            if t not in teams:
                teams[t] = 0

    counter = 0
    for i in competitions:
        if results[counter] == 0:
            teams[i[1]] += 3
        else:
            teams[i[0]] += 3
        counter += 1
    winner = None
    for i in teams:
        if winner == None:
            winner = i
        elif teams[i] > teams[winner]:
            winner = i
    return winner

print(tournamentWinner(competitions,results))