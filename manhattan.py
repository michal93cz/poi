import psycopg2
import psycopg2.extras
from pprint import pprint
from timeit import default_timer as timer

from utils import get_objects_amenity_count, get_PIs, get_PRs


def manhattan_measure(first_object, second_object):
  # this is in wikipedia and another sources but gives wrong results
  # return abs(first_object['object_long'] - first_object['object_lat']) + abs(second_object['object_long'] - second_object['object_lat'])
  return abs(second_object.object_long - first_object.object_long) + abs(second_object.object_lat - first_object.object_lat)

def main_algorithm_manhattan(treshold):
  conn = psycopg2.connect("dbname=detroit_large user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  cur.execute('SELECT * FROM objects')

  objects = cur.fetchall()

  cur.close()

  objects_prim = objects.copy()

  result = []
  dictionary = {}

  i = 0
  for object_i in objects:
    # print(i)
    # i += 1

    objects_prim.remove(object_i)

    for object_j in objects_prim:
      distance = manhattan_measure(object_i, object_j)

      if distance <= treshold:
        result.append((object_i, object_j, distance))
  
  return result

amenities = get_objects_amenity_count()
# print(manhattan_measure({'object_long': 4, 'object_lat': 3}, {'object_long': 1, 'object_lat': 1}))
treshold = 500

# pprint(main_algorithm_manhattan(treshold))
start = timer()
result = main_algorithm_manhattan(treshold)
end = timer()
duration = end - start

f = open("./results/detroit_large_manhattan.txt", "w+")
f.write('Duration: %d s \r\n' % duration)

print('Duration: ', duration, 's')

PRs = get_PRs(result, amenities)
PIs = get_PIs(PRs, amenities)

f.write('Number of collocations: %d\r\n' % len(PIs))

for PI in PIs:
  f.write(str(PI) + '\n')

f.close()
