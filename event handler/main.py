from tkinter import *
window=Tk()
window.title("EVENT HANDLER")
window.geometry("100x100")

def handler_click(event):
    print("The button is clicked")

def key_presed(event):
    print("the key presed is ",event.char)
button=Button(text="click me")
button.pack()

button.bind("<Button-1>",handler_click)
window.bind("<Key>",key_presed)
window.mainloop()