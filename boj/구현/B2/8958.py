n = int(input())

for i in range(n):
    question = input()
    seriesScore = 0
    total = 0
    for alpha in question:
        if alpha == "O":
            seriesScore += 1
        else:
            seriesScore = 0
        total += seriesScore
    print(total)
