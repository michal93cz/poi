import psycopg2
import psycopg2.extras


def search_in_array_of_dicts(array, key, value):
  for item in array:
    if item[key] == value:
      return item

def get_edges_by_start_and_end_node_postgres(edge_id, node_type):
  conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  if node_type == 'start':
    cur.execute('SELECT e2.edge_id FROM edges e1, edges e2 WHERE e1.edge_id <> e2.edge_id AND e1.edge_id = %s AND (ST_Equals(e1.start_node, e2.start_node) OR ST_Equals(e1.start_node, e2.end_node))',
    [edge_id])
  else:
    cur.execute('SELECT e2.edge_id FROM edges e1, edges e2 WHERE e1.edge_id <> e2.edge_id AND e1.edge_id = %s AND (ST_Equals(e1.end_node, e2.start_node) OR ST_Equals(e1.end_node, e2.end_node))',
    [edge_id])

  edges = cur.fetchall()

  for edge in edges:
    print(edge.edge_id)

  cur.close()

  return edges

def get_node_edges(node_geom):
  conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  cur.execute('SELECT e.edge_id FROM edges e WHERE ST_Equals(e.start_node, %s) OR ST_Equals(e.end_node, %s)', [node_geom, node_geom])

  edges = cur.fetchall()

  cur.close()

  return edges

def get_edge_by_id(edge_id):
  conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  cur.execute('SELECT * FROM edges WHERE edge_id = %s', [edge_id])

  edge = cur.fetchone()

  cur.close()

  return edge

def get_edge_objects(edge_id):
  conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
  cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

  cur.execute('SELECT * FROM objects WHERE edge_id = %s', [edge_id])

  objects = cur.fetchall()

  cur.close()

  return objects
