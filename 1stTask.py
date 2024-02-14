import csv

with open('game.txt') as file:
    reader = csv.reader(file)
    data = list(reader)


def findReplace(data):
    for row in data:
        for i in range(len(row)-1):
            if '55' in row[i]:
                row[i] = 'Done'
                row[i+1] = '0000-00-00'
                return row


bug_error = findReplace(data)

with open('game_new.csv', "w", encoding='utf8', newline='') as file:
    print(data)
    writer = csv.writer(file)
    writer.writerows(data)