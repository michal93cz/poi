import psycopg2


conn = psycopg2.connect("dbname=gis user=postgres password=postgres")
cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)

cur.close()