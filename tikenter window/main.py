from tkinter import *
window=Tk()
window.title("my first demo")
window.geometry('300x400')
lbl=Label(text="welcome",fg="white",bg="black",height=2,width=300)
lbl.pack()
namelabel=Label(text="enter your name",fg="white",bg="black",height=4,width=300)
namelabel.pack()
name_enter=Entry()
name_enter.pack()
def display():
   name=name_enter.get()
   Message="welcome to the application"
   greet="hello "+name+"\n"
   textbox.insert(END,greet)
   textbox.insert(END,Message)
textbox=Text(height=5)
textbox.pack()
btn=Button(text="tap me",command=display,height=2,fg="white",bg="black")
btn.pack()
window.mainloop()