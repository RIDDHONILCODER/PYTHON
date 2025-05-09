
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    # if a file is opened then display the contents of the file
    with open(filepath, "r") as input_file:
        # Read contents of the input file
        text = input_file.read()
        # Insert contents of the file in the editor box
        txt_edit.insert(END, text)
        input_file.close()
        window.title(f"Codingal's Text Editor - {filepath}")
def save_file():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
    if not filepath:
       return
    with open(filepath, "w") as output_file:
        # Read the edited content and update in the output file
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        window.title(f"Codingal's Text Editor - {filepath}")
        
window=Tk()
window.title("Riddhonil's text editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
txt_edit=Text(window)
frame_button=Frame(window,relief=RAISED,bd=2)
open_button=Button(frame_button,text="open",command=open_file)
save_button=Button(frame_button,text="save as",command=save_file)
open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
frame_button.grid(row=0,column=0,sticky="ns",)
window.mainloop()