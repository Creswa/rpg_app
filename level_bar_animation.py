import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title, size):

        super().__init__()

            # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        self.columnconfigure((0), weight = 1, uniform = "a")

        

        bar_width = 600
        bar_height = 20

        canvas_bar = tk.Canvas(self, width=bar_width, height=bar_height, bg="white", highlightthickness=0)
        canvas_bar.grid(row=0, column=0, sticky="ew")

        fill_width = int(bar_width/4) # místo 4 *exp
        color = "green" #barva přiřazená skillu
        canvas_bar.create_rectangle(0, 0, fill_width, bar_height, fill=color) 
        canvas_bar.create_rectangle(fill_width, 0, bar_width, bar_height, fill="#ddd")

        # Text na progress baru
        canvas_bar.create_text(bar_width//2, bar_height//2,
                                text="Skibidi", # to, co je teď na labelu dole
                                fill="black")

        self.mainloop()

App("test", (600,600))
