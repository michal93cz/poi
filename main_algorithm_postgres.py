from pprint import pprint
import psycopg2
import psycopg2.extras

from edge_expansion_postgres import edge_expansion
from neighbor_objects_refining_postgres import neighbor_objects_refining

conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

cur.execute('SELECT * FROM edges LIMIT 13')

edges = cur.fetchall()

threshold = 1000

def ens(edges, threshold):
  ST = []

  for edge in edges:
    EDC = edge_expansion(edge, threshold)

    for tuple in EDC:

      if tuple[3] <= threshold:
        STC = neighbor_objects_refining(tuple, threshold)
        ST.append(STC)

  return ST

pprint(ens(edges, threshold))
# ens(edges, threshold, nodes)
