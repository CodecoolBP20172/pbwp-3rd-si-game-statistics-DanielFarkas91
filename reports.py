
def count_games(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        game_list = []
        for line in text:
            words = line.split("\t")
            game_list.append(words[0]) 
        return (len(game_list))


def decide(file_name, year):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()
        year = str(year)
        for line in text:
            words = line.split("\t")
            if words[2] == year:
                return True
        return False
    txt_file.close()


def get_latest(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()

        games_with_dates = {}
        for line in text:
            words = line.split("\t")
            games_with_dates[words[0]] = words[2]
        
        sorted_games_with_dates = sorted(games_with_dates.items(), key=lambda x: x[1])
        latest_game_with_date = sorted_games_with_dates[-1]
        return latest_game_with_date[0]


def count_by_genre(file_name, genre):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()

        genre_list = []
        for line in text:
            words = line.split("\t")
            genre_list.append(words[3])

        for genre in genre_list:
            count_genre = genre_list.count(genre)
        
        return count_genre


def get_line_number_by_title(file_name, title):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()

        line_number = 0
        while True:
            try:
                for i in text:
                    words = i.split("\t")
                    line_number += 1
                    if words[0] == title:
                        return line_number
            
                if words[0] != title:
                    raise ValueError

            except ValueError:
                print("This title is not in the list")
                break


def sort_abc(file_name):
    with open(file_name, mode='r') as txt_file:
            text = txt_file.readlines()

            abc_list = []
            for line in text:
                words = line.split("\t")
                abc_list.append(words[0])
            
            return sorted(abc_list)


def get_genres(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()

        genres_list = {}
        for line in text:
            words = line.split("\t")
            genres_list[words[3]] = 1
        
        genres_list = list(sorted(genres_list.keys(), key=str.lower))
        return genres_list


def when_was_top_sold_fps(file_name):
    with open(file_name, mode='r') as txt_file:
        text = txt_file.readlines()

        while True:
            try:
                genres_dict = {}
                for line in text:
                    words = line.split("\t")
                    if words[3] == "First-person shooter":
                        genres_dict[float(words[1])] = int(words[2])

                if words[3] != "First-person shooter":
                    raise ValueError

                sorted_dict = sorted(genres_dict.items(), key=lambda x: float(x[0]), reverse=True)
                return sorted_dict[0][1]

            except ValueError and IndexError:
                return "There is no game with genre 'First-person shooter'"
