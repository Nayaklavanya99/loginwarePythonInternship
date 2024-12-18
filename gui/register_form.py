from tkinter import *

window = Tk()

window.geometry("1920x1080")
window.title("Entry Box")
# ent = Entry(window, width=20)
file_path = "form.docs"
# ent.place(x=20, y=10)
valx=100
valy=100
global list1
list1 = ["Name","age","Number","EmailId","College","Course","Usn","Gender"]
list2 = list1

for i in list1:  
    lbl2 = Label(window, text=i, fg="blue", font=("Jokerman", 15))
    lbl2.place(x=valx, y=valy)
    # valx += 50
    valy +=50
valx=200
valy=100
for i in range(len(list1)-1):
    list1[i] = Entry(window, width=40)
    list1[i].place(x=valx, y=valy)
    # valx
    valy+=50

def fileformat():
    with open(file_path,"a") as file:
            file.write("----------------------------------------------------------------------------------\n")
def send():
    list3 = ["Name","age","Number","EmailId","College","Course","Usn"]
    fileformat()
    for i in range(len(list1)):
        
        print(f"{list3[i]} : {list1[i].get()}")
        with open(file_path,"a") as file:
            file.write(f"{list3[i]} : {list1[i].get()}\n")
        list1[i].delete(0,END)  
    print(choice.get())  
# def click():
    # with open(file_path,"a") as file:
    #         file.write(f"Gender : {choice.get()}\n")    
    
choice= StringVar()
genders = ["Male","Female","Others"]
x,y=200,450
for i in genders:
    
    radio_btn1 = Radiobutton(window, text=i, value=i,font=("Arial",15),variable=choice)

    radio_btn1.place(x=x,y=y)
    y+=50

btn = Button(window, text="Send", command=send,bg="green",fg="white",font=("bold",15))
btn.place(x=530, y=valy+190)


window.mainloop()