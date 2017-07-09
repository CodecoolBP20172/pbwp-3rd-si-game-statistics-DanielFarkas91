import math


def main():
    print(words("game_stat.txt", 4))
    print(get_most_played("game_stat.txt"))
    print(sum_sold("game_stat.txt"))
    print(get_selling_avg("game_stat.txt"))
    print(count_longest_title("game_stat.txt"))
    print(get_date_avg("game_stat.txt"))
    print(get_game("game_stat.txt", "Guild Wars"))
    print(count_grouped_by_genre("game_stat.txt"))
    print(get_date_ordered("game_stat.txt"))


# bonus function: splitting textlines into coloums.
def words(file_name, y):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        game_list = []
        for line in text:
            words = line.strip("\n").split("\t")
            game_list.append(words[y])
        return game_list


# test 1
def get_most_played(file_name):
    most_played_games = zip([float(i) for i in words(
        file_name, 1)], words(file_name, 0))
    sorted_games = sorted(most_played_games, key=lambda x: float(x[0]))
    return sorted_games[-1][1]


# test 2
def sum_sold(file_name):
    return sum(float(i) for i in words(file_name, 1))


# test 3
def get_selling_avg(file_name):
    return sum_sold(file_name) / len(words(file_name, 1))


# test 4
def count_longest_title(file_name):
    count_title_list = sorted([len(i) for i in words(file_name, 0)])
    return count_title_list[-1]


# test 5
def get_date_avg(file_name):
    return math.ceil(sum([float(i) for i in words(
        file_name, 2)]) / len([float(i) for i in words(file_name, 2)]))


# test 6
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


# bonus 1
def count_grouped_by_genre(file_name):
    genre_count = {}
    for i in words(file_name, 3):
        if i in genre_count.keys():
            genre_count[i] += 1
        else:
            genre_count.update({i: 1})
    return genre_count


# bonus 2
def get_date_ordered(file_name):
    x = sorted(sorted(zip([int(i) for i in words(file_name, 2)], [
        i for i in words(file_name, 0)]), key=lambda x: x[1]),
        key=lambda x: x[0], reverse=True)
    x = list(x)
    x = [b for a, b in x]
    return x


main()
