def main():
    print(get_most_played("game_stat.txt"))
    print(sum_sold("game_stat.txt"))
    print(get_selling_avg("game_stat.txt"))
    print(count_longest_title("game_stat.txt"))


# bonus function words[y]
def words(file_name, y):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        game_list = []
        for line in text:
            words = line.split("\t")
            game_list.append(words[y])
        return game_list


# 1test
def get_most_played(file_name):
    most_played_games = zip((float(i) for i in words(file_name, 1)), words(file_name, 0))
    most_played_games = dict(most_played_games)
    sorted_games = sorted(most_played_games.items(), key=lambda x: float(x[0]), reverse=True)
    return sorted_games[0][1]


# 2test
def sum_sold(file_name):
    return sum(float(i) for i in words(file_name, 1))


# 3 test
def get_selling_avg(file_name):
    return sum_sold(file_name) / len(words(file_name, 1))


# 4 test
def count_longest_title(file_name):
    pass


main()
