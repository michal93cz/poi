from pprint import pprint
import psycopg2
import psycopg2.extras
import numpy
import itertools
from timeit import default_timer as timer

from edge_expansion_postgres import edge_expansion
from neighbor_objects_refining_postgres import neighbor_objects_refining
from utils import get_PRs, get_PIs, get_objects_amenity_count


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

conn = psycopg2.connect("dbname=detroit_large user=postgres password=postgres")
cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

cur.execute('SELECT * FROM edges')

edges = cur.fetchall()
amenities = get_objects_amenity_count()
threshold = 500

start = timer()
collocations = ens(edges, threshold, cur)
end = timer()
duration = end - start

cur.close()

f = open("./results/detroit_large_ens.txt", "w+")
f.write('Duration: %d s \r\n' % duration)

PRs = get_PRs(collocations, amenities)
PIs = get_PIs(PRs, amenities)

f.write('Number of collocations: %d\r\n' % len(PIs))

for PI in PIs:
  f.write(str(PI) + '\n')

f.close()
