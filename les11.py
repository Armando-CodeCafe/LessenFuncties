from tkinter import *

window = Tk()
# window.geometry("1280x720")


# def plus():
#     numA=0
#     numB=0
#     try:
#         numA = int(a.get())
#         numB = int(b.get())
#     except:
#         print("Number error")
#         return
#     label["text"] = str(numA+numB)
# def keer():
#     numA = 0
#     numB = 0
#     try:
#         numA = int(a.get())
#         numB = int(b.get())
#     except:
#         print("Number error")
#         return
#     label["text"] = str(numA * numB)
#
#
# label = Label(master = window,text="Antwoord=0",background="#ffef08",
#               foreground='#2130ff',font=("Arial",20,'bold'),width=20,height=2)
# label.pack()
def onclick(waarde):
    label["text"]= waarde
    pass
num = 1
button = Button(master=window,text=num,font=("Arial",30),command=lambda waarde = num: onclick(waarde) )
label = Label(master=window,text="Hoi",font=("Arial",30))
label.pack()
button.pack()
# b = 4
# h =3
#
# for rij in (range(h)):
#     for kolom in range(b):
#         num = (kolom+1)+(rij*b)
#
#         label = Label(master=window,text=str(num),font=("Arial",40))
#         label.grid(row= rij,column = kolom,pady = 5,padx= 5)

# top = Frame(master = window,background="red")
# top.pack(fill="x")
#
# button1 = Button(master=top,text="Button1")
# button1.pack(side =LEFT)

#
# a = Entry(master=window, font =("Arial",40))
# b = Entry(master=window, font =("Arial",40))
# a.pack(pady=20)
# b.pack()
#
# plus = Button(master=window,text="PLUS",command=plus)
# keer = Button(master=window,text="KEER",command=keer)
# plus.pack()
# keer.pack()



window.mainloop()