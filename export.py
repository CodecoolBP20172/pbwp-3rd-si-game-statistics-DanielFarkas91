from reports import (
    count_games, decide, get_latest, count_by_genre,
    get_line_number_by_title, sort_abc, get_genres, when_was_top_sold_fps)


def main():
    txt_file = "game_stat.txt"
    year = 2012
    genre = "First-person shooter"
    title = "Guild Wars"
    exported_values = [
        count_games(txt_file), decide(
            txt_file, year), get_latest(
                txt_file), count_by_genre(
                    txt_file, genre), get_line_number_by_title(
                        txt_file, title), sort_abc(txt_file),  get_genres(
                            txt_file), when_was_top_sold_fps(txt_file)]

    with open("export.txt", mode='w') as txt_file:
        for i in exported_values:
            txt_file.writelines((str(i), "\n"))


main()
