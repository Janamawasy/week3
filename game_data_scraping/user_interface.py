import processing
import visualization
def handle_input(freq, data):
    print('choose one of this genres:')
    for i, genre in enumerate(freq.keys()):
        print(f'Enter {i+1} for this genre: {genre}')
    choice = input('Enter your choice ')
    if int(choice)>0 and int(choice)<=len(freq):
        selected_genre = list(freq.keys())[int(choice) - 1]
        per = processing.calculate_percentage(freq, selected_genre, data)
        print(per)
        visualization.pie_plot(per, selected_genre)
    else:
        print('invalid input')

