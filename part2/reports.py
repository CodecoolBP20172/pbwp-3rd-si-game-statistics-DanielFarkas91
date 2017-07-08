import math


# bonus function words[y]
def words(file_name, y):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        game_list = []
        for line in text:
            words = line.strip("\n").split("\t")
            game_list.append(words[y])
        return game_list


def get_most_played(file_name):
    most_played_games = zip([float(i) for i in words(
        file_name, 1)], words(file_name, 0))
    sorted_games = sorted(most_played_games, key=lambda x: float(x[0]))
    return sorted_games[-1][1]


def sum_sold(file_name):
    return sum(float(i) for i in words(file_name, 1))


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(words(file_name, 1))


def count_longest_title(file_name):
    count_title_list = sorted([len(i) for i in words(file_name, 0)])
    return count_title_list[-1]


def get_date_avg(file_name):
    return math.ceil(sum([float(i) for i in words(
        file_name, 2)]) / len([float(i) for i in words(file_name, 2)]))


def get_game(file_name, title):
    property_list = []
    n = 0
    for i in words(file_name, 0):
        if i == title:
            for z in range(0, 5):
                property_list.append(words(file_name, z)[n])
        else:
            n += 1
    property_list[1] = float(property_list[1])
    property_list[2] = int(property_list[2])
    return property_list
