import psycopg2 as pg
import psycopg2.extras as pge
conn = pg.connect("host = 'localhost' dbname = 'stationszuil' user ='postgres' password=''")
cursor = conn.cursor(cursor_factory=pge.RealDictCursor)