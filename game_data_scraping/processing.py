import re

def populate_data(results):
    data={}
#     data = { game_name: [ genres ], }
    top_results = results[:10]
    for i in top_results:
        game_name = i.find('div',class_='tab_item_name').get_text()
        all_genres = i.find_all('span', class_='top_tag')
        genres = []
        for genre in all_genres:
            res = regx_text(genre.get_text())
            genres.append(res)
        data[game_name] = genres
    return data

def regx_text(text):
    res = re.sub(r'[, ]+', '', text)
    # Trimming leading and trailing spaces
    res = res.strip()
    return res

def calculate_genre_freq(data):
    freq = {}
    # freq = { genre_name : freq }
    for genrs_lst in data.values():
        for genre_name in genrs_lst:
            if genre_name in freq.keys():
                freq[genre_name] += 1
            else:
                freq[genre_name] = 1
    return freq

def calculate_percentage(freq, genre, data):
    if freq[genre]:
        per = freq[genre]/len(data)
        return per * 100


