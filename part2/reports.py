# bonus function words[y]
def words(file_name, y):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        game_list = []
        for line in text:
            words = line.split("\t")
            game_list.append(words[y])
        return game_list


def get_most_played(file_name):
    most_played_games = zip((float(i) for i in words(file_name, 1)), words(file_name, 0))
    most_played_games = dict(most_played_games)
    sorted_games = sorted(most_played_games.items(), key=lambda x: float(x[0]), reverse=True)
    return sorted_games[0][1]


def sum_sold(file_name):
    return sum(float(i) for i in words(file_name, 1))


def get_selling_avg(file_name):
    return sum_sold(file_name) / len(words(file_name, 1))
