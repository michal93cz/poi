from pprint import pprint

from utils import get_edge_objects, get_edge_by_id


def neighbor_objects_refining(tuple, threshold, cursor):
  STC = []

  e_objects = get_edge_objects(tuple[0], cursor)
  # pprint(e_objects)

  # print('-------------------------------')
  e_prim_objects = get_edge_objects(tuple[1], cursor)
  # pprint(e_prim_objects)
  e = get_edge_by_id(tuple[0], cursor)
  e_prim = get_edge_by_id(tuple[1], cursor)


  # my invention:
  e_objects_copy = e_objects.copy()
  for object in e_objects:
    e_objects_copy.remove(object)

    for object_prim in e_objects_copy:
      ND = abs(object.pos - object_prim.pos)

      if ND <= threshold:
         STC.append((object, object_prim, ND))


  for object_i in e_objects:
    for object_j in e_prim_objects:
      # objects in the same edge is omitted
      ND = 0
      ET = tuple[2]
      ED = tuple[3]

      if ET == 'SS':
        ND = object_i.pos + ED + object_j.pos

      if ET == 'SE':
        ND = object_i.pos + ED + e_prim.weight - object_j.pos

      if ET == 'ES':
        ND = ED + e.weight - object_i.pos + object_j.pos

      if ET == 'EE':
        ND = ED + e.weight - object_i.pos + e_prim.weight - object_j.pos

      if ND <= threshold:
         STC.append((object_i, object_j, ND))

  return STC
