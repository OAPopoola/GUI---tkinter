from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("DSR Start Page")
window.geometry('400x300')

seaLabel = Label(window,text = "Subject Email Address:")
seaEntry = Entry(window)
idLabel = Label(window,text = "Identity ID:")
idEntry = Entry(window)
snLabel = Label(window,text = "Subject Name:")
snEntry = Entry(window)
rdLabel = Label(window,text = "Received Date:")
rdEntry = Entry(window)
actLabel = Label(window,text = "Action Required:")

cbb = Combobox(window)
cbb['values']= ("SAR", "Deletion", "Both") 
cbb.current(0) #set the selected item 


ddLabel = Label(window,text = "Due Date:")
ddEntry = Entry(window)
snumLabel = Label(window,text = "S - Number:")
snumEntry = Entry(window)
dnumLabel = Label(window,text = "D - Number:")
dnumEntry = Entry(window)
nLabel = Label(window,text = "Notes:")
nEntry = Entry(window)

seaEntry.grid(row = 0, column = 1)
seaLabel.grid(row = 0, column = 0)
idLabel.grid(row = 1, column = 0)
idEntry.grid(row = 1, column = 1)
snLabel.grid(row = 2, column = 0)
snEntry.grid(row = 2, column = 1)
rdLabel.grid(row = 3, column = 0)
rdEntry.grid(row = 3, column = 1)
actLabel.grid(row = 4, column = 0)
cbb.grid(column=1, row=4)
ddLabel.grid(row = 5, column = 0)
ddEntry.grid(row = 5, column = 1)
snumLabel.grid(row = 6, column = 0)
snumEntry.grid(row = 6, column = 1)
dnumLabel.grid(row = 7, column = 0)
dnumEntry.grid(row = 7, column = 1)
nLabel.grid(row = 8, column = 0)
nEntry.grid(row = 8, column = 1)




def clearAll():
    #tk.messagebox.showinfo("Clicked", "This is just a alert message!")
    pass
    
    
def processEntry():
    res = "The Email Address is: " + seaEntry.get()
    print(res)
    

pBbtn = Button(text = "Process SAR", command = processEntry).grid(row = 9, column = 0)
cBtn = Button(text = "Clear",command = clearAll).grid(row = 9, column = 1)

window.mainloop()

