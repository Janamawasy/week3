import matplotlib.pyplot as plt

def plot_tags(freq):
    plt.figure(figsize=(10, 6))
    plt.bar(freq.keys(), freq.values())
    plt.title('Top 10 Most Appeared Tags in Popular Games')
    plt.xlabel('Tag')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def pie_plot(per,genre):
    y = [per, 100-per]
    mylabels = [genre, 'other genres']
    plt.pie(y, labels = mylabels)
    plt.title('selected genre percentage')
    plt.show()



