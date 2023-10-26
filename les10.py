import datetime

import psycopg2 as pg
import psycopg2.extras as pge
conn_string ="host='localhost' dbname ='stationszuil' user='postgres' password=''"

conn = pg.connect(conn_string)
cur = conn.cursor(cursor_factory=pge.RealDictCursor) # maakt cursor aan, cursor factory bepaald wat voor datatype de queries returnen

def insert_into_database(dictionary):
    query = ("""INSERT INTO berichten(naam,achternaam,bericht,datum)
                VALUES(%s,%s,%s,%s)
        """)
    cur.execute(query, (dictionary["naam"], dictionary["achternaam"], dictionary["bericht"], dictionary["datum"]))
def module1(cur):

    naam = input("Naam: ")
    achternaam = input("Achternaam: ")
    bericht = input("Bericht")
    datum = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_into_database({"naam":naam,"achternaam":achternaam,"bericht":bericht,"datum": datum})


module1(cur)



conn.commit()
conn.close()
def foo(a,b,c=10,d):
    print(a,b,c)
foo(15,20,c=30)
