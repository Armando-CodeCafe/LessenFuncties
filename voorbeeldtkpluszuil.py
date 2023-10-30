from tkinter import *
import psycopg2 as pg
import psycopg2.extras

conn_data = "host='localhost' dbname='stationszuil' user='postgres' password=''"
conn = pg.connect(conn_data)

cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

window = Tk()
window.geometry("1920x1080")
left = Frame(window,background="yellow")
left.pack(side = LEFT, fill="both")
right = Frame(window,background="blue")
right.pack(side = RIGHT, fill="both")


title = Label(left,background="yellow",foreground="blue",text = "Welkom bij staationszuil \nvan 'station'",font=("Helvetica",30,'bold'))
title.pack(side=TOP)

def get_top_messages():

    cur.execute("SELECT * FROM berichten ORDER BY date LIMIT 5")
    gets = cur.fetchall()
    print(gets)
    return gets
def draw_messages(messages,frame):
    pass

draw_messages(get_top_messages())





window.mainloop()