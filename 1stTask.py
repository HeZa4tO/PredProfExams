# Первая задача, которая стоит перед вами это найти все ошибки с содержанием числа 55,
# тк это особо важные и опасные ошибки. Для этого составьте отчет в формате: “У персонажа\t<characters>\tв игре\t
# <GameName>\tнашлась ошибка с кодом:\t <nameError>.\tДата фиксации:\t <date>”. После предоставления отчета измените значение
# ошибки на “Done”, а в поле дата поставьте “0000-00-00”  и полученные измененные данные сохраните в файле game_new.csv
# (загрузите файл в поле ответа).
#
# В задаче запрещено использование сторонних библиотек


def ReplaceData():
    with open('game.txt', encoding="utf8") as reader, open('game_new.csv', 'w', encoding="utf8") as writer:
        game_data = []
        header = next(reader)

        for i in reader:
            s = i.split('$')
            if '55' in (s[-2][-3:]):
                s[-2] = 'Done'
                s[-1] = '0000-00-00\n'
                game_data.append(header)
                writer.write(game_data)
                writer.close()


if __name__ == '__main__':
    ReplaceData()
