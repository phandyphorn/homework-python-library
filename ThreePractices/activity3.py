import tkinter as tk
manyBoxs = tk.Tk()
manyBoxs.geometry("600x600")
manyColorBoxs = tk.Frame()
manyColorBoxs.master.title("PNC UI GAME")

canvas = tk.Canvas(manyColorBoxs)
import random;
boxColors = ["#FF0000","#0000FF","#008000","#FFA500","#FFFF00","#000000","#800080"]
for i in range(9):
    for index in range(9):
        canvas.create_rectangle(10+25*i,20+25*index,30+25*i,40+25*index,fill= random.choice(boxColors))
canvas.pack(expand=True, fill = "both")
manyColorBoxs.pack(expand=True, fill = "both")
manyColorBoxs.mainloop()