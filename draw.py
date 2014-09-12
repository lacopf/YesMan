from Tkinter import *
import tkMessageBox
import ttk
import os

blank = " "
for i in range(0,50):
	blank = blank + " "


root = Tk()
root.title("I'm Yesman!")

mainframe = ttk.Frame(root, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

img = PhotoImage(file='/home/lacopf/Documents/YesMan/yesman.gif')
label = ttk.Label(mainframe).grid(column=3, row=1)

question = StringVar()
response = StringVar()
response.set("How can I help you?")

feet_entry = ttk.Entry(mainframe, width=30, textvariable=question)
feet_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, image=img).grid(column=1, row=2, sticky=(W, E))

yesmanText = ttk.Label(mainframe, text=response.get(), width= len(response.get()) ).grid(column=1, row=1)

def respond(*args):
	p = question.get()
	response.set(p)
	resp = "I'm sorry, I can't answer " + p + " yet"

	if 

	ttk.Label(mainframe, text=blank, width=len(blank)).grid(column=1, row=1 )
	ttk.Label(mainframe, text=resp, width=len(resp)).grid(column=1, row=1 )

ttk.Button(mainframe, text="Ask", command=respond).grid(column=2, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=10, pady=10)

feet_entry.focus()
root.bind('<Return>', respond)

root.mainloop()