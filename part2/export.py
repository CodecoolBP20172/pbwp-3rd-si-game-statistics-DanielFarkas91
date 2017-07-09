from reports import (
    get_most_played, sum_sold, get_selling_avg,
    count_longest_title, get_date_avg, get_game,
    count_grouped_by_genre, get_date_ordered)


def main():
    export_file = "game_stat.txt"
    title = "Guild Wars"

    exported_values = [get_most_played(
        export_file), sum_sold(
            export_file), get_selling_avg(
                export_file), count_longest_title(
                export_file), get_date_avg(
                    export_file), get_game(
                        export_file, title),count_grouped_by_genre(
                            export_file), get_date_ordered(export_file)]

    with open("export.txt", mode='w') as txt_file:
        for i in exported_values:
            txt_file.writelines((str(i), "\n"))


main()
