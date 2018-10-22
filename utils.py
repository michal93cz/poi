import psycopg2
import psycopg2.extras


def search_in_array_of_dicts(array, key, value):
  for item in array:
    if item[key] == value:
      return item

def get_edges_by_start_and_end_node_postgres(edge_id, node_type, cur):
  if node_type == 'start':
    cur.execute('SELECT e2.edge_id FROM edges e1, edges e2 WHERE e1.edge_id <> e2.edge_id AND e1.edge_id = %s AND (ST_Equals(e1.start_node, e2.start_node) OR ST_Equals(e1.start_node, e2.end_node))',
    [edge_id])
  else:
    cur.execute('SELECT e2.edge_id FROM edges e1, edges e2 WHERE e1.edge_id <> e2.edge_id AND e1.edge_id = %s AND (ST_Equals(e1.end_node, e2.start_node) OR ST_Equals(e1.end_node, e2.end_node))',
    [edge_id])

  edges = cur.fetchall()

  for edge in edges:
    print(edge.edge_id)

  return edges

def get_node_edges(node_geom, cur):
  cur.execute('SELECT e.edge_id FROM edges e WHERE ST_Equals(e.start_node, %s) OR ST_Equals(e.end_node, %s)', [node_geom, node_geom])

  edges = cur.fetchall()

  return edges

def get_edge_by_id(edge_id, cur):
  cur.execute('SELECT * FROM edges WHERE edge_id = %s', [edge_id])

  edge = cur.fetchone()

  return edge

def get_edge_objects(edge_id, cur): 
  cur.execute('SELECT * FROM objects WHERE edge_id = %s', [edge_id])

  objects = cur.fetchall()

  return objects

def get_objects_amenity_count():
  conn = psycopg2.connect("dbname=moskwa_large user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

  cur.execute('SELECT object_amenity, COUNT(*) FROM objects GROUP BY object_amenity')

  amenities = cur.fetchall()

  cur.close()

  return dict(amenities)

def get_PIs(PRs, amenities):
  # amenities = get_objects_amenity_count()
  result = {}

  for PR in PRs:
    min = 1

    for amenity, ids in PR.items():
      partial_PR = len(ids) / amenities[amenity]
      if partial_PR < min:
        min = partial_PR
    
    keys = list(PR.keys())
    if len(keys) < 2:
      result[(keys[0], keys[0])] = min
    else:
      result[(keys[0], keys[1])] = min

  return sorted(result.items(), key=lambda x: x[1], reverse=True)

def get_PRs(collocations, amenities):
  dictionary = {}
  # amenities = get_objects_amenity_count()

  for collocation in collocations:
    key = (collocation[0].object_amenity, collocation[1].object_amenity)
    key2 = (collocation[1].object_amenity, collocation[0].object_amenity)
    if key in dictionary.keys():
      dictionary[key] = 0
    elif key2 in dictionary.keys():
      dictionary[key2] = 0
    else:
      dictionary[key] = 0
  
  PRs = []
  for key in dictionary.keys():
    # key[0] and key[1] can be the same
    keys_participation = { key[0]: [], key[1]: [] }
    for collocation in collocations:
      if (collocation[0].object_amenity == key[0] and collocation[1].object_amenity == key[1]) or (collocation[1].object_amenity == key[0] and collocation[0].object_amenity == key[1]):
        if not collocation[0].object_id in keys_participation[collocation[0].object_amenity]:
          keys_participation[collocation[0].object_amenity].append(collocation[0].object_id)

        if not collocation[1].object_id in keys_participation[collocation[1].object_amenity]:
          keys_participation[collocation[1].object_amenity].append(collocation[1].object_id)

    PRs.append(keys_participation)

  return PRs
