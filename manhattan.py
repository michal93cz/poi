import psycopg2
import psycopg2.extras
from pprint import pprint

from utils import get_objects_amenity_count, get_PIs, get_PRs


def manhattan_measure(first_object, second_object):
  # this is in wikipedia and another sources but gives wrong results
  # return abs(first_object['object_long'] - first_object['object_lat']) + abs(second_object['object_long'] - second_object['object_lat'])
  return abs(second_object.object_long - first_object.object_long) + abs(second_object.object_lat - first_object.object_lat)

def main_algorithm_manhattan(treshold):
  conn = psycopg2.connect("dbname=detroit user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  cur.execute('SELECT * FROM objects')

  objects = cur.fetchall()

  cur.close()

  objects_prim = objects.copy()

  result = []
  dictionary = {}

  for object_i in objects:
    objects_prim.remove(object_i)

    for object_j in objects_prim:
      distance = manhattan_measure(object_i, object_j)

      if distance <= treshold:
        result.append((object_i, object_j, distance))
  
  return result


# print(manhattan_measure({'object_long': 4, 'object_lat': 3}, {'object_long': 1, 'object_lat': 1}))
treshold = 200

# pprint(main_algorithm_manhattan(treshold))
result = main_algorithm_manhattan(treshold)

PRs = get_PRs(result)
# pprint(PRs)

PIs = get_PIs(PRs) 
for PI in PIs[:50]:
  print(PI)
