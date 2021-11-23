import tkinter as tk
rec = tk.Tk()
rec.geometry("600x600")
fiveBoxs = tk.Frame()
fiveBoxs.master.title("PNC UI GAME")

canvas = tk.Canvas(fiveBoxs)

# red rectangle
canvas.create_rectangle(90,90,360,360, fill="#FF0000")

# blue rectangle
canvas.create_rectangle(120,120,330,330, fill="#0000FF")

# green rectangle
canvas.create_rectangle(150,150,300,300, fill="#008000")

# yellow rectangle
canvas.create_rectangle(180,180,270,270, fill="#FFA500")


# green rectangle smaller
canvas.create_rectangle(200,200,250,250, fill="#008000")


canvas.pack(expand=True, fill='both')
fiveBoxs.pack(expand=True, fill='both')
fiveBoxs.mainloop()