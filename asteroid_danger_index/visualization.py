import matplotlib.pyplot as plt

def plot_tags(dict, A , B ,C):
    plt.figure(figsize=(10, 6))
    plt.bar(dict.keys(), dict.values())
    plt.title(f'Danger index for each asteroid with A = {A}, B = {B} and C = {C}')
    plt.xlabel('Asteroid Name')
    plt.ylabel('Danger Index')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_min_diameter_velocity():
    pass

def plot_dis_max_diameter():
    pass