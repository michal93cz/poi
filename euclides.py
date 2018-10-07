import math


def euclides_measure(first_point, second_point):
  return math.sqrt((second_point['x'] - first_point['x'])^2 + (second_point['y'] - first_point['y'])^2)

print(euclides_measure({'x': 1, 'y': 1}, {'x': 3, 'y': 3}))
