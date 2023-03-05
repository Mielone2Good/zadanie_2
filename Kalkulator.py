from tkinter import *


root = Tk()
root.title("Kalkulator")
root.geometry("300x400")
root.resizable(False,False)
root.configure(bg="#616060")

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")

def wynik():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:

        equation.set(" blad ")
        expression = ""


equation = StringVar()
expression_field = Entry(root,width=20, textvariable=equation,font=("Helvetica","15","bold"))
expression_field.place(x=40,y=90)
clear = Button(root,width=30,bg="red", text="Clear",command=clear,font=("Helvetica","8","bold"))
clear.place(x=40,y=135)

one = Button(root,text="1",width=3 ,bg="grey",command=lambda: press(1),font=("Helvetica","15","bold")).place(x=40,y=290)
two = Button(root,text="2",width=3 ,bg="grey",command=lambda: press(2),font=("Helvetica","15","bold")).place(x=100,y=290)
three = Button(root,text="3",width=3 ,bg="grey",command=lambda: press(3),font=("Helvetica","15","bold")).place(x=160,y=290)
four = Button(root,text="4",width=3 ,bg="grey",command=lambda: press(4),font=("Helvetica","15","bold")).place(x=40,y=230)
five = Button(root,text="5",width=3 ,bg="grey",command=lambda: press(5),font=("Helvetica","15","bold")).place(x=100,y=230)
six = Button(root,text="6",width=3 ,bg="grey",command=lambda: press(6),font=("Helvetica","15","bold")).place(x=160,y=230)
seven = Button(root,text="7",width=3 ,bg="grey",command=lambda: press(7),font=("Helvetica","15","bold")).place(x=40,y=170)
eight = Button(root,text="8",width=3 ,bg="grey",command=lambda: press(8),font=("Helvetica","15","bold")).place(x=100,y=170)
nine = Button(root,text="9",width=3 ,bg="grey",command=lambda: press(9),font=("Helvetica","15","bold")).place(x=160,y=170)
zero = Button(root,text="0",width=3 ,bg="grey",command=lambda: press(0),font=("Helvetica","15","bold")).place(x=100,y=350)

plus = Button(root,text="+",width=3 ,bg="lightgrey",command=lambda: press("+"),font=("Helvetica","15","bold")).place(x=220,y=350)
minus = Button(root,text="-",width=3 ,bg="lightgrey",command=lambda: press("-"),font=("Helvetica","15","bold")).place(x=220,y=290)
mnozenie = Button(root,text="*",width=3 ,bg="lightgrey",command=lambda: press("*"),font=("Helvetica","15","bold")).place(x=220,y=230)
dzielenie = Button(root,text="/",width=3 ,bg="lightgrey",command=lambda: press("/"),font=("Helvetica","15","bold")).place(x=220,y=170)

wynikB = Button(root,text="=",width=3 ,bg="lightgrey",command=wynik,font=("Helvetica","15","bold")).place(x=160,y=350)
przecinek = Button(root,text=",",width=3 ,bg="lightgrey",command=lambda: press("."),font=("Helvetica","15","bold")).place(x=40,y=350)







root.mainloop()