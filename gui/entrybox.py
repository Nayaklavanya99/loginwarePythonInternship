from tkinter import *
windows = Tk()
print("window opened")
windows.geometry("860x540")
windows.title("notepad")
windows.configure(bg="white")
def showtext():
    print(input1.get())
    ver = input1.get()
    global entrylabel
    entrylabel = Label(windows,text=input1.get(),fg="blue",bg="white",font=("Jokerman",20,"bold","underline"),justify="center")
    entrylabel.place(x=300,y=100,width=300,height=100)
    input1.delete(0,END)
    
input1 = Entry(windows,bd=2,width=50,bg="lightblue")

input1.place(x=0,y=10)
btn = Button(windows,text="send",command=showtext,bg="green")
btn.place(x=350,y=10)




















windows.mainloop()