from pymongo import MongoClient
from tkinter import *
client = MongoClient()
db = client['euro-bund-10y']
coll=db['rawdata']
cursor = coll.find()
i=0;

master = Tk()
frame=Frame(master,width=300,height=800)
frame.grid(row=0,column=0)
w = Canvas(frame, width=300, height=800,scrollregion=(0,0,300,1000))
vbar=Scrollbar(frame,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=w.yview)
w.config(yscrollcommand=vbar.set)
w.pack(side=LEFT,expand=True,fill=BOTH)
y=50
x=0
z=y+25
coordinates={}
for document in cursor:
    if i==0:
        firstAskS=document['ask']
        firstAsk=float(firstAskS)-0.10
        endAsk=firstAsk+0.20
        while(firstAsk<endAsk):
            ask = w.create_text(x, y, anchor="sw")
            formatedFloat="{0:.2f}".format(firstAsk)
            coordinate={firstAsk,x,y}
            coordinates[formatedFloat]=coordinate
            w.itemconfig(ask, text=formatedFloat)
            firstAsk=firstAsk+0.01
            y=y+25;
        master.update_idletasks()
        master.update()
    i = i + 1
    if i > 1000:
        break
    """
    
    document
    w.create_rectangle(x + 50, y, 150, y + 25, fill="red")
    w.create_rectangle(x, z, 150, z+25, fill="blue")
    if document['type']== "Z":
        ask = w.create_text(x + 50, y,anchor="sw")
        w.itemconfig(ask, text=document['ask'])
    y=y+25
    z=z+25
    if i>1000:
        break
    master.update_idletasks()
    master.update()
    """

    print(document)
mainloop()

