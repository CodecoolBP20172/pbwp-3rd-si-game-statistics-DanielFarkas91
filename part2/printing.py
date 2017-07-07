def main():
    # print(get_most_played("game_stat.txt"))
    print(sum_sold("game_stat.txt"))


# 1test
def get_most_played(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        most_played_games = {}
        for line in text:
            words = line.split("\t")
            most_played_games[(float(words[1]))] = words[0]

        sorted_games = sorted(most_played_games.items(), key=lambda x: float(x[0]), reverse=True)
        return sorted_games[0][1]


# 2test
def sum_sold(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        sold_games = []
        for line in text:
            words = line.split("\t")
            sold_games.append(float(words[1]))
        sum_sold_games = sum(sold_games)
        return sum_sold_games
        


main()
