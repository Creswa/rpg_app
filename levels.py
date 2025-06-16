import tkinter as tk
from tkinter import ttk

level = 0
exp = 0

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        self.experience = 0
        self.level = 0
        self.skill = NewSkill(self, self.adding_exp, self.subtracting_exp, self.level, self.experience)

        self.mainloop()
    
    def adding_exp(self):
        self.experience += 1
        print(self.experience)
    
    def subtracting_exp(self):
        self.experience -= 1
        print(self.experience)
    
    def show_exp(self):
        print (self.experience)

class NewSkill(ttk.Frame):
    def __init__(self, parent, plus_exp_callback, minus_exp_callback, level, experience):
        super().__init__(parent)
        self.plus_exp_callback = plus_exp_callback
        self.minus_exp_callback = minus_exp_callback
        self.level = level
        self.experience = experience
        self.experience_needed = 5
        self.create()
        self.pack(fill="x", pady=5)

    def create(self):
        new_skill_frame = ttk.Frame(self, height=50, borderwidth=5, relief="solid")
        new_skill_frame.pack_propagate(False)
        new_skill_frame.pack(fill="x")

        new_skill_frame.columnconfigure(0, weight=3)
        new_skill_frame.columnconfigure(1, weight=2)
        new_skill_frame.columnconfigure((2, 3), weight=1, uniform="a")
        new_skill_frame.rowconfigure((0, 1), weight=1)

        skill_name = ttk.Label(new_skill_frame, text= "sex", anchor="w", borderwidth=1, relief="solid")
        level = ttk.Label(new_skill_frame, text=f"Level: {self.level}", anchor="w", borderwidth=1, relief="solid")
        plus_button = ttk.Button(new_skill_frame, text="+", command = self.plus_exp_callback)
        minus_button = ttk.Button(new_skill_frame, text="-", command = self.minus_exp_callback)
        level_bar = tk.Label(new_skill_frame, text=f"XP {self.experience}/{self.experience_needed}", anchor="center", borderwidth=2,relief="solid", background="red")

        skill_name.grid(row=0, column=0, sticky="nsew")
        level.grid(row=0, column=1, sticky="nsew")
        plus_button.grid(row=0, column=2, sticky="nsew")
        minus_button.grid(row=0, column=3, sticky="nsew")
        level_bar.grid(row=1, column=0, columnspan=4, sticky="nsew")

if __name__ == "__main__":
    App("Class based app", (400, 400))