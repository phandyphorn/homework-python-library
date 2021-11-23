import tkinter as tk
oval = tk.Tk()
oval.geometry("600x600")
fiveOvals = tk.Frame()
fiveOvals.master.title("PNC UI GAME")
canvas = tk.Canvas(fiveOvals)

# red oval
canvas.create_oval(90,90,360,360, fill="#FF0000")

# blue oval
canvas.create_oval(120,120,330,330, fill="#0000FF")

# green oval
canvas.create_oval(150,150,300,300, fill="#008000")

# yellow oval
canvas.create_oval(180,180,270,270, fill="#FFA500")

# green oval smaller
canvas.create_oval(200,200,250,250, fill="#008000")


canvas.pack(expand=True, fill='both')
fiveOvals.pack(expand=True, fill='both')
fiveOvals.mainloop()