import csv
# Первая задача, которая стоит перед вами это найти все ошибки с содержанием числа 55,
# тк это особо важные и опасные ошибки. Для этого составьте отчет в формате: “У персонажа\t<characters>\tв игре\t
# <GameName>\tнашлась ошибка с кодом:\t <nameError>.\tДата фиксации:\t <date>”. После предоставления отчета измените значение
# ошибки на “Done”, а в поле дата поставьте “0000-00-00”  и полученные измененные данные сохраните в файле game_new.csv
# (загрузите файл в поле ответа).
#
# В задаче запрещено использование сторонних библиотек

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