from pprint import pprint
import psycopg2
import psycopg2.extras
import numpy
import itertools

from edge_expansion_postgres import edge_expansion
from neighbor_objects_refining_postgres import neighbor_objects_refining
from utils import get_PRs, get_PIs


def ens(edges, threshold, cursor): 
  ST = []

  i = 0
  for edge in edges:
    print(i)
    i += 1

    EDC = edge_expansion(edge, threshold, cursor)

    for tuple in EDC:
      # print(tuple)
      if tuple[3] <= threshold:
        STC = neighbor_objects_refining(tuple, threshold, cursor)
        ST.append(STC)

  return list(itertools.chain.from_iterable(ST))

conn = psycopg2.connect("dbname=moskwa user=postgres password=postgres")
cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

cur.execute('SELECT * FROM edges')

edges = cur.fetchall()
threshold = 200

collocations = ens(edges, threshold, cur)
cur.close()

# pprint(collocations)

PRs = get_PRs(collocations)
PIs = get_PIs(PRs)

for PI in PIs[:20]:
  print(PI)
