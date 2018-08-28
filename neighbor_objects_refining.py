from pprint import pprint


def neighbor_objects_refining(tuple, threshold):
  STC = []

  for object_i in tuple[0]['objects']:
    for object_j in tuple[1]['objects']:
      ND = 0
      e = tuple[0]
      e_prim = tuple[1]
      ET = tuple[2]
      ED = tuple[3]

      if ET == 'SS':
        ND = object_i['pos'] + ED + object_j['pos']

      if ET == 'SE':
        ND = object_i['pos'] + ED + e_prim['weight'] - object_j['pos']

      if ET == 'ES':
        ND =  ED + e['weight'] - object_i['pos'] + object_j['pos']

      if ET == 'EE':
        ND = ED + e['weight'] - object_i['pos'] + e_prim['weight'] - object_j['pos']

      if ND <= threshold:
        STC.append((object_i, object_j, ND))

  return STC
