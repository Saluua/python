from tkinter import *

def cercle (can,x,y,r):
    can.create_oval(x-r,y-r,x+r,y+r)
    
class Application (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.can= Canvas(self,width=535,height=130,bg='ivory')
        self.can.pack(side= TOP, padx=5,pady=5)
        self.dessiner()


    def dessiner(self):
        self.w1= Wagon(self.can,10,30)


class Wagon():
    def __init__(self,can,x,y):
        self.can = can
        self.x = x
        self.y = y
        can.create_rectangle(x,y,x+110,y+60)
        for i in range (x+5,x+86,35):
            can.create_rectangle(i,y+5,x+30,y+40)
        cercle (can , x+20,y+70,10)
        cercle (can , x+90,y+70,10)
    



app=Application()

app.mainloop()
