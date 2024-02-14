def binary_search(character, games):
    """
    Функция для двоичного поиска персонажа в игре
    :param character: имя персонажа
    :param games: список игр
    :return: индекс первого вхождения персонажа или -1, если он не найден
    """
    left = 0
    right = len(games) - 1

    while left <= right:
        middle = (left + right) // 2
        if character == games[middle]:
            return middle
        elif character < games[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def main():
    with open('game.txt', encoding="utf8") as file:
        games = sorted(file.read().splitlines())
        while True:
            character = input('Введите имя персонажа или "game" для выхода ')

            if character == 'game':
                break

            index = binary_search(character, games)

            if index != -1:
                print(f'Персонаж {character} встречается в играх:')
                for i in range(index, min(index + 5, len(games))):
                    print(games[i])
                if index + 5 < len(games):
                    print('и др.')
            else:
                print('Этого персонажа не существует.')


if __name__ == '__main__':
    main()