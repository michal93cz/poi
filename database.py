import psycopg2
import psycopg2.extras
from pprint import pprint


conn = psycopg2.connect("dbname=moskwa_large user=postgres password=postgres")
cur = conn.cursor(cursor_factory = psycopg2.extras.NamedTupleCursor)

cur.execute('SELECT * FROM edges')

edges = cur.fetchall()
print(edges[0].edge_id)
# for edge in edges:
#   print(edge[0])

cur.close()
