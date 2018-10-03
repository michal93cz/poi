import psycopg2


conn = psycopg2.connect("dbname=moskwa user=postgres password=postgres")
cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()')

db_version = cur.fetchone()
print(db_version)

cur.execute('SELECT PostGIS_full_version()')

postgis_version = cur.fetchone()
print(postgis_version)

cur.execute('select count(*) FROM planet_osm_point where ((tags->\'man_made\') = \'tower\')')

count = cur.fetchone()
print(count)

cur.close()
