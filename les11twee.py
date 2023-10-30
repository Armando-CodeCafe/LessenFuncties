from tkinter import *

window = Tk()
#window.geometry("1280x720")

# def onclick():
#     base=0
#     expo= 0
#     try:
#         base = int(entry.get())
#         expo = base**2
#     except:
#         label["text"]="Vul aub een nummer in"
#         label["background"] = "red"
#         return
#     label["text"] =expo
#     label["background"] = "#ffdc14"
#
# label = Label(window,text="Hallo wereld",background="#ffdc14",
#               foreground="#3347ff", font=("Arial",30,'bold'), height=2)
# # img = PhotoImage(file = "ns.png")
# # label = Label(window,image = img)
# label.pack()
#
# button =Button(window,text="Klik mij",
#                background="pink",
#                foreground="yellow",font=("Arial",30,'bold'),command=onclick)
# button.pack(pady = 20)
#
# entry = Entry(window,font=("Arial",20))
# entry.pack()
# def plus():
#     numA = int(entry1.get())
#     numB = int(entry2.get())
#     antwoord["text"] = numA+numB
# def keer():
#     numA = int(entry1.get())
#     numB = int(entry2.get())
#     antwoord["text"] = numA * numB
font = ("Arial",15)
# kant = TOP
# antwoord = Label(window,text="Antwoord = 0",font=font)
# antwoord.pack(side = kant)
#
# entry1 = Entry(window,font= font)
# entry2 = Entry(window,font= font)
# entry1.pack(side = kant,pady=15)
# entry2.pack(side = kant,pady=15)
#
# plusButton = Button(window,text="Plus",font = font,command=plus)
# keerButton = Button(window,text="Keer",font = font,command=keer)
# plusButton.pack(side = kant,pady=15)
# keerButton.pack(side = kant)
#
# fillLabel = Label(window,text="fill x",background="yellow",font=font)
# fillLabel.pack()

# top = Frame(window,background="red")
# top.pack(fill ="x")
#
# button = Button(top,text="Knop top")
# button.pack(side = LEFT)
# button1 = Button(top,text="Knop top")
# button1.pack(side = LEFT)

# b= 4
# h =3
#
# for rij in range(h):
#     for kol in range(b):
#         num = (kol+1)+(rij*b)
#         label = Label(window,text=num,font =font )
#         label.grid(row = rij, column = kol,padx = 10,pady=10)

def change(rij,kol):
    label["text"] = opties[rij][kol]
opties = [
    ("1","2","3","+"),
    ("4","5","6","-"),
    ("7","8","9","*"),
    ("+/-","0","=","/")

]
box = Frame(window)
box.pack(fill="x")
grid = Frame(window)
grid.pack(fill="x")
label = Label(box,text=0,highlightcolor="gray",highlightbackground="white",font = font)
label.pack()

for row in range(4):
    for col in range(4):
        rij = row
        kol = col
        button = Button(grid,text=opties[row][col],width=4,height=4,command=lambda r = rij,c = kol: change(r,c) ,font = font)
        button.grid(row = row,column = col)
window.mainloop()