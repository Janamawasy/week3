import fetching_data
import processing
import user_interface
import visualization


def main():
    url = "https://store.steampowered.com/"
    soup = fetching_data.fetch_data(url)
    results = fetching_data.fetch_popular_games_data(soup)
    data = processing.populate_data(results)
    freq = processing.calculate_genre_freq(data)
    visualization.plot_tags(freq)
    user_interface.handle_input(freq, data)

if __name__ == '__main__':
    main()
