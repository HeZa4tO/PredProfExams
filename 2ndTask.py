def read_data(file_name):
    """
    Функция для чтения данных их файла
    :param file_name: Имя файла
    :return: список данных
    """
    with open('game.txt', encoding="utf8") as file:
        data = file.readlines()
    return data


def sort_data(data):
    """
    Функция сортировки по столбцу игры
    :param data: список данных
    :return: sorted_data отсортированный список данных
    """
    sorted_data = sorted(data, key=lambda x: x.split(',')[0])
    return sorted_data


def generate_report(sorted_data):
    """
    Функция для генерации отчета о количестве багов в каждой игре
    :param sorted_data: отсортированный список данных
    """
    report = {}
    for row in sorted_data:
        game = row.split('$')[0]
        if game in report:
            report[game] += 1
        else:
            report[game] = 1
    for game, count in report.items():
        print(f'{game} - количество багов: {count}')


data = read_data('game.txt')
sorted_data = sort_data(data)
generate_report(sorted_data)
