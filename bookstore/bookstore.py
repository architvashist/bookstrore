from tkinter import *
import backend
window = Tk()


def get_selected_row(event):
    try:
        data=l1.get(ANCHOR)
        e1.delete(0,END)
        e1.insert(END,data[1])    
        e2.delete(0,END)
        e2.insert(END,data[2])
        e3.delete(0,END)
        e3.insert(END,data[3])
        e4.delete(0,END)
        e4.insert(END,data[4])
    except IndexError:
        pass



def view_command():
    l1.delete(0,END)
    for row in backend.view():
        l1.insert(END,row)

def search_command():
    l1.delete(0,END)
    for row in backend.search(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()):
        l1.insert(END,row)

def add_command():
    backend.insert(title_var.get(),author_var.get(),year_var.get(),isbn_var.get())
    l1.delete(0,END)
    l1.insert(END,(title_var.get(),author_var.get(),year_var.get(),isbn_var.get()))
    view_command()
    

def delete_command():
    backend.delete(l1.get(ANCHOR)[0])
    view_command()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_command():
    data=l1.get(ANCHOR)
    backend.update(data[0],title_var.get(),author_var.get(),year_var.get(),isbn_var.get())
    view_command()


l1=Label(window,text="Title")
l1.grid(row=0,column=0)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
l3=Label(window,text="Year")
l3.grid(row=1,column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_var=StringVar()
e1=Entry(window,textvariable=title_var)
e1.grid(row=0,column=1)

author_var=StringVar()
e2=Entry(window,textvariable=author_var)
e2.grid(row=0,column=3)
year_var=StringVar()
e3=Entry(window,textvariable=year_var)
e3.grid(row=1,column=1)
isbn_var=StringVar()
e4=Entry(window,textvariable=isbn_var)
e4.grid(row=1,column=3)



sb1=Scrollbar(window,orient=VERTICAL)
sb1.grid(row=2,column=2,rowspan=6)

l1=Listbox(window,width=25,yscrollcommand=sb1.set)
l1.grid(row=2,column=0,rowspan=6,columnspan=2)

l1.bind("<<ListboxSelect>>",get_selected_row)

sb1.configure(command=l1.yview)




b1=Button(window,width=12,text="View all",command=view_command)
b1.grid(row=2,column=3)
b1=Button(window,width=12,text="Search entry",command=search_command)
b1.grid(row=3,column=3)
b1=Button(window,width=12,text="Add entry",command=add_command)
b1.grid(row=4,column=3)
b1=Button(window,width=12,text="Delete",command=delete_command)
b1.grid(row=5,column=3)
b1=Button(window,width=12,text="Update",command=update_command)
b1.grid(row=6,column=3)
b1=Button(window,width=12,text="Close",command=window.destroy)
b1.grid(row=7,column=3)


window.resizable(0,0)
window.wm_title("Book Store")
window.mainloop()
