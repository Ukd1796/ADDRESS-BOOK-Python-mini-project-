from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import sqlite3
Profile = {1:""}

#addDetails
def Add_Details():
    name = EnterN.get()
    phone = EnterP.get()
    address = Enteraddress.get()
    #connecting database
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    cur.execute("INSERT INTO detail ('Name','PHONE','Address') values(?,?,?)",(name,phone,address))
    connector.commit()
    connector.close()
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    select = cur.execute("SELECT * FROM detail ORDER BY ID desc ")
    select = list(select)
    data.insert('', END ,values = select[0])
    connector.close()
    #adding photo && connecting through database
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    select = cur.execute("SELECT * FROM detail ORDER BY ID desc ")
    select = list(select)
    id = select[0][0]
    fileN = EnterI.get()
    Im = Image.open(fileN)
    Converted_Im = Im.convert('RGB')
    Converted_Im.save(("images/profile_"+ str(id) + "."+"jpg"))
    connector.close()


#delete details
def Delete_details():
    SerialNo = data.item(data.selection())['values'][0]
    connector=sqlite3.connect("database.db")
    cur = connector.cursor()
    delete = cur.execute("delete from detail where ID = {}".format(SerialNo))
    connector.commit()
    data.delete(data.selection())

#sort details
def SortByName():
    for i in data.get_children():
        data.delete(i)
    connector = sqlite3.connect("database.db")
    cur = connector.cursor()
    selection = cur.execute("select*from detail order by Name asc ")
    connector.commit()
    for row in selection:
        data.insert('',END,values = row)
    connector.close()

#update details
def Update_Details():
    SerialNo = data.item(data.selection())['values'][0]
    connector=sqlite3.connect("database.db")
    cur = connector.cursor()
    delete = cur.execute("delete from detail where ID = {}".format(SerialNo))
    connector.commit()
    data.delete(data.selection())
    name = EnterN.get()
    phone = EnterP.get()
    address = Enteraddress.get()
    #connecting database
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    cur.execute("INSERT INTO detail ('Name','PHONE','Address') values(?,?,?)",(name,phone,address))
    connector.commit()
    connector.close()
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    select = cur.execute("SELECT * FROM detail ORDER BY ID desc ")
    select = list(select)
    data.insert('', END ,values = select[0])
    connector.close()
    #adding photo && connecting through database
    connector = sqlite3.connect('database.db')
    cur = connector.cursor()
    select = cur.execute("SELECT * FROM detail ORDER BY ID desc ")
    select = list(select)
    id = select[0][0]
    fileN = EnterI.get()
    Im = Image.open(fileN)
    Converted_Im = Im.convert('RGB')
    Converted_Im.save(("images/profile_"+ str(id) + "."+"jpg"))
    connector.close()

#search by name
def SearchbyName(event):
    for i in data.get_children():
        data.delete(i)
    name = AB_placetosearchN.get()
    connector = sqlite3.connect("database.db")
    cur = connector.cursor()
    selection = cur.execute("SELECT*FROM detail where Name = (?)",(name,))
    connector.commit()
    for i in selection:
        data.insert("",END,values=i)
    connector.close()

#search by phoneNO
def SearchbyPhoneNo(event):
    for i in data.get_children():
        data.delete(i)
    phone = AB_placetosearchP.get()
    connector = sqlite3.connect("database.db")
    cur = connector.cursor()
    selection = cur.execute("SELECT*FROM detail where PHONE = (?)",(phone,))
    connector.commit()
    for i in selection:
        data.insert("",END,values=i)
    connector.close()

#adding images
def BrowsePhoto():
    EnterI.delete(0,END)
    filename = filedialog.askopenfile(initialdir = "/",title="SELECT FILE")
    EnterI.insert(END,filename)

#displaying details
def treeActionSelect(event):
    Image_label.destroy()
    idselect = data.item(data.selection())['values'][0]
    Nselect = data.item(data.selection())['values'][1]
    Pno_select = data.item(data.selection())['values'][2]
    Addselect = data.item(data.selection())['values'][3]
    Profileimg = "images/profile_"+ str(idselect) + "."+"jpg"
    load = Image.open(Profileimg)
    load.thumbnail((200,200))
    photo_person = ImageTk.PhotoImage(load)
    Profile[1]=photo_person
    I_label = Label(r,image=photo_person)
    I_label.place(x=10,y=320)
    displayId = Label(r,text = "ID: "+str(idselect))
    displayId.place(x=10,y=440)
    displayName = Label(r,text = "Name: "+Nselect)
    displayName.place(x=10,y=460)
    displayNo = Label(r,text = "Phone: "+str(Pno_select))
    displayNo.place(x=10,y=480)
    Text_address = Text(r)
    Text_address.place(x=260,y=360,width=230,height=120)
    Text_address.insert(END,"Address : "+str(Addselect))




#dimensions determination
r = Tk()
r.title("Address book(Python Mini Project)")
r.geometry('500x550')
#title
ABtitle = Label(r,text="Address Book",font=("Arial",22), bg="black",fg="white")
ABtitle.place(x=0,y=0,width=250)
#search
AB_searchbyname = Label(r,text="Search by Name:",bg="black",fg="white")
AB_searchbyname.place(x=250,y=0,width=120)
AB_placetosearchN = Entry(r)
AB_placetosearchN.bind("<Return>",SearchbyName)
AB_placetosearchN.place(x=380,y=0,width=160)
AB_searchbyphone = Label(r,text="Search by PhoneNO:",bg="black",fg="white")
AB_searchbyphone.place(x=250,y=18,width=120)
AB_placetosearchP = Entry(r)
AB_placetosearchP.bind("<Return>",SearchbyPhoneNo)
AB_placetosearchP.place(x=380,y=20,width=160)

#main_window
AB_name=Label(r,text="Enter Name:",bg="black",fg="white")
AB_name.place(x=5,y=50,width=125)
EnterN = Entry(r)
EnterN.place(x=140,y=50,width=400)
#phone_NO
AB_Phone=Label(r,text="Enter PhoneNO:",bg="black",fg="white")
AB_Phone.place(x=5,y=80,width=125)
EnterP = Entry(r)
EnterP.place(x=140,y=80,width=400)
#photo
AB_Photo=Label(r,text="Photo:",bg="black",fg="white")
AB_Photo.place(x=5,y=110,width=125)
b_Browse=Button(r,text="Browse",bg="white",fg="black",command = BrowsePhoto)
b_Browse.place(x=425,y=107,height=25,width=70)
EnterI = Entry(r)
EnterI.place(x=140,y=110,width=280)

#address
AB_address=Label(r,text="Enter Address:",bg="black",fg="white")
AB_address.place(x=5,y=140,width=125)
Enteraddress = Entry(r)
Enteraddress.place(x=140,y=140,width=400)

#buttons
B_add=Button(r,text="Create a new contact",bg="brown",fg="white",command = Add_Details)
B_add.place(x=5,y=170,width=255)
B_delete=Button(r,text="Delete the selected contact",bg="brown",fg="white",command = Delete_details)
B_delete.place(x=5,y=195,width=255)
B_update=Button(r,text="Update the selected contact",bg="brown",fg="white",command = Update_Details)
B_update.place(x=5,y=220,width=255)
B_sort=Button(r,text="Sort by name",bg="brown",fg="white",command = SortByName)
B_sort.place(x=5,y=245,width=255)
B_exit=Button(r,text="Exit",bg="brown",fg="white",command = quit)
B_exit.place(x=5,y=270,width=255)

#image
load = Image.open("images/icon.png")
load.thumbnail((130,130))
locationofImage = ImageTk.PhotoImage(load)
Image_label = Label(r,image=locationofImage)
Image_label.place(x=10,y=320)

#data display box
data = ttk.Treeview(r,columns=(1,2,3,4),height=5,show="headings")
data.place(x=265,y=170,width=290,height=175)
data.bind("<<TreeviewSelect>>",treeActionSelect)

# add scrollbar
scrolllb = ttk.Scrollbar(r,orient="vertical",command=data.yview)
scrolllb.place(x=480,y=170,height=175)
data.configure(yscrollcommand=scrolllb.set)
data.heading(1, text = "SerialNo")
data.heading(2, text = "Name")
data.heading(3, text = "phoneNO")
data.heading(4,text="Address")
#defining_width
data.column(1,width=55)
data.column(2,width=100)
data.column(3,width=110)
#displaying data in box(connecting it)
connector = sqlite3.connect('database.db')
cur = connector.cursor()
selection = cur.execute("select*from detail")
for row in selection:
    data.insert('',END,value=row)


r.mainloop()





