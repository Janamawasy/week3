def populate_data(data):
    dt = {}
    for i in data:
        dt[i] = filter_data(data[i][0])
        # dt[i] = {}
        # dt[i]['id'] = data[i][0]['id']
        # dt[i]['name'] = data[i][0]['name']
        # dt[i]['estimated_diameter_min'] = data[i][0]['estimated_diameter']['kilometers']['estimated_diameter_min']
        # dt[i]['estimated_diameter_max'] = data[i][0]['estimated_diameter']['kilometers']['estimated_diameter_max']
        # dt[i]['relative_velocity'] = data[i][0]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
        # dt[i]['miss_distance'] = data[i][0]['close_approach_data'][0]['miss_distance']['kilometers']
    return dt

def filter_data(data):
    res = {}
    res['id'] = data['id']
    res['name'] = data['name']
    res['estimated_diameter_min'] = data['estimated_diameter']['kilometers']['estimated_diameter_min']
    res['estimated_diameter_max'] = data['estimated_diameter']['kilometers']['estimated_diameter_max']
    res['relative_velocity'] = data['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']
    res['miss_distance'] = data['close_approach_data'][0]['miss_distance']['kilometers']
    return res
def populate_month_data(month_list):
    q = {}
    for dict in month_list:
        for key in dict.keys():
            q[key] = filter_data(dict[key][0])
    print(q)
    return q

def danger_calculator(data, A, B, C):
    danger_dict = {}
    for ast in data:
        avrage_diameter = 0.5*(int(data[ast]['estimated_diameter_max'])+int(data[ast]['estimated_diameter_min']))
        danger = A* avrage_diameter +( (B / C) * float(data[ast]['relative_velocity'])* float(data[ast]['miss_distance']))
        danger_dict[data[ast]['name']] = danger
    return danger_dict