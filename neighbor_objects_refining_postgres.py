from pprint import pprint

from utils import get_edge_objects, get_edge_by_id


def neighbor_objects_refining(tuple, threshold):
  STC = []

  e_objects = get_edge_objects(tuple[0])
  e_prim_objects = get_edge_objects(tuple[1])
  e = get_edge_by_id(tuple[0])
  e_prim = get_edge_by_id(tuple[1])

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
         STC.append((object_i.object_amenity, object_j.object_amenity, ND))

  return STC