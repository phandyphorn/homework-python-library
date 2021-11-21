# =====Answer the question:====
# In this drawing, there are:
# + 4 rectangles
# + 5 ovals


import tkinter as tk
box = tk.Tk()
box.geometry("300x300")
boxName = tk.Frame()
boxName.master.title("Hello PNC")


canvas = tk.Canvas(boxName)
# left eye
canvas.create_oval(40,40,100,70, fill ="#FFF")
canvas.create_oval(55,40,85,70,fill="#0000FF",outline="#0000FF" )

# right eye
canvas.create_oval(160,40,220,70, fill="#FFF")
canvas.create_oval(175,40,205,70,fill="#0000FF",outline="#0000FF")

# nose
canvas.create_oval(115,130,145,160,fill="#FF0000",outline="#FF0000" )

# a little black on nose
canvas.create_rectangle(128,130,132,131,fill="#000000" )

# left mouse
canvas.create_rectangle(40,190,50,220,fill="#FF0000",outline="#FF0000" )

# center mouse
canvas.create_rectangle(40,220,210,230,fill="#FF0000",outline="#FF0000" )

# right mouse
canvas.create_rectangle(210,205,220,230,fill="#FF0000",outline="#FF0000")



canvas.pack(expand=True, fill='both')
boxName.pack(expand=True, fill='both')

box.mainloop()