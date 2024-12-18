from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
def submit():
    print(nameEntry.get())
    nameEntry.delete(0,END)
    nameEntry.insert(3,"hello")
    print(ageEntry.get())
    ageEntry.delete(0,END)
    print(numEntry.get())
    numEntry.delete(0,END)
  

nameLabel = Label(windows,text="Name: ",fg="blue",bg="white",font=("Jokerman",10,"bold"),justify="center")  
nameLabel.place(x=0,y=10)  
nameEntry = Entry(windows,bd=2,width=80,bg="lightblue")
nameEntry.place(x=80,y=10)



ageLabel = Label(windows,text="Age: ",fg="blue",bg="white",font=("Jokerman",10,"bold"),justify="center")  
ageLabel.place(x=0,y=80)  
ageEntry = Entry(windows,bd=2,width=80,bg="lightblue")
ageEntry.place(x=80,y=80)


numLabel = Label(windows,text="Number: ",fg="blue",bg="white",font=("Jokerman",10,"bold"),justify="center")  
numLabel.place(x=0,y=120)  
numEntry = Entry(windows,bd=2,width=80,bg="lightblue")
numEntry.place(x=80,y=120)

sub_btn = Button(windows,text="send",command=submit,bg="green")
sub_btn.place(x=200,y=300)




windows.mainloop()