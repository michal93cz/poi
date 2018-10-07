from pprint import pprint
import psycopg2
import psycopg2.extras
import numpy
import itertools

from edge_expansion_postgres import edge_expansion
from neighbor_objects_refining_postgres import neighbor_objects_refining
from utils import get_PRs, get_PIs

conn = psycopg2.connect("dbname=poznan user=postgres password=postgres")
cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

cur.execute('SELECT * FROM edges LIMIT 13')

edges = cur.fetchall()

threshold = 200

def ens(edges, threshold): 
  ST = []

  i = 0
  for edge in edges:
    print(i)
    i += 1

    EDC = edge_expansion(edge, threshold)

    for tuple in EDC:
      if tuple[3] <= threshold:
        STC = neighbor_objects_refining(tuple, threshold)
        ST.append(STC)

  return list(itertools.chain.from_iterable(ST))

collocations = ens(edges, threshold)

pprint(collocations)

PRs = get_PRs(collocations)
pprint(get_PIs(PRs))
