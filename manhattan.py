def manhattan_measure(first_point, second_point):
    return abs(second_point['x'] - first_point['x']) + abs(second_point['y'] - first_point['y'])

print(manhattan_measure({'x': 0, 'y': 0}, {'x': 2, 'y': 3}))
