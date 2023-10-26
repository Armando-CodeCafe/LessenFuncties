#simulatie van module 1
import datetime as dt
import connect as c

def nieuw_bericht():
    voornaam = input("voornaam: ")
    achternaam = input("Achternaam: ")
    bericht = input ("Bericht: ")
    date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {"voornaam":voornaam,"achternaam":achternaam,"bericht":bericht, "datum": date}

def insert_bericht(bericht):
    c.cursor.execute("INSERT INTO berichten (naam,achternaam,bericht,datum) VALUES(%s,%s,%s,%s)",(bericht["voornaam"],bericht["achternaam"],bericht["bericht"],bericht["datum"]))
    c.conn.commit()
def check_berichten():
    c.cursor.execute("SELECT * FROM berichten")
    for r in c.cursor.fetchall():
        print(r["datum"])
check_berichten()
#insert_bericht(nieuw_bericht())