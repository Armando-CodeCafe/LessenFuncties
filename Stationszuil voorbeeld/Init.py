#voorbeeld van stationzuil
import connect


connect.cursor.execute("""CREATE TABLE IF NOT EXISTS berichten(
                id SERIAL PRIMARY KEY,
                naam varchar(30),
                achternaam varchar(50),
                bericht varchar(255) NOT NULL,
                datum TIMESTAMP NOT NULL);""")
connect.conn.commit()
connect.conn.close()