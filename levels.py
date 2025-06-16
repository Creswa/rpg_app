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

        self.experience = tk.IntVar(value = 0)
        self.level = tk.IntVar(value = 1)

        self.skill = NewSkill(self, self.level, self.experience)

        self.mainloop()
    

class NewSkill(ttk.Frame):
    def __init__(self, parent, level, experience):
        super().__init__(parent)
        self.level = level
        self.experience = experience
        self.level_bar = None
        self.level_number = None
        self.experience_needed = 5 * self.level.get()
        self.create()
        self.pack(fill="x", pady=5)

        self.experience.trace_add("write", self.update_level_bar)
        self.level.trace_add("write", self.update_level)

    def adding_exp(self):
        self.experience.set(self.experience.get() + 1)
        print(self.experience.get())
    
    def subtracting_exp(self):
        self.experience.set(self.experience.get() - 1)
        print(self.experience.get())
    
    def add_level(self):
        self.level.set(self.level.get() + 1)

    def update_level_bar(self, *args):
        if self.level_bar:
            self.level_bar.config(
                text = f"XP {self.experience.get()}/{self.experience_needed}"
            )
    def update_level(self, *args):
        self.experience_needed = 5 * self.level.get() #updates level and needed exp
        if self.level_number:
            self.level_number.config(
                text = f"Level: {self.level.get()}"

            )
            self.level_bar.config(
               text = f"XP{self.experience.get()}/{self.experience_needed}" 
            )
    def create(self):
        new_skill_frame = ttk.Frame(self, height=50, borderwidth=5, relief="solid")
        new_skill_frame.pack_propagate(False)
        new_skill_frame.pack(fill="x")

        new_skill_frame.columnconfigure(0, weight=3)
        new_skill_frame.columnconfigure(1, weight=2)
        new_skill_frame.columnconfigure((2, 3), weight=1, uniform="a")
        new_skill_frame.rowconfigure((0, 1,2), weight=1)

        skill_name = ttk.Label(new_skill_frame, text= "sex", anchor="w", borderwidth=1, relief="solid")
        self.level_number = ttk.Label(new_skill_frame, text=f"Level: {self.level.get()}", anchor="w", borderwidth=1, relief="solid")
        plus_button = ttk.Button(new_skill_frame, text="+", command = self.adding_exp)
        minus_button = ttk.Button(new_skill_frame, text="-", command = self.subtracting_exp)
        self.level_bar = tk.Label(new_skill_frame, text = f"XP{self.experience.get()}/{self.experience_needed}", anchor="center", borderwidth=2,relief="solid")
        test_add_level_button = ttk.Button(new_skill_frame, text = "Add level", command = self.add_level).grid(row = 2)

        skill_name.grid(row=0, column=0, sticky="nsew")
        self.level_number.grid(row=0, column=1, sticky="nsew")
        plus_button.grid(row=0, column=2, sticky="nsew")
        minus_button.grid(row=0, column=3, sticky="nsew")
        self.level_bar.grid(row=1, column=0, columnspan=4, sticky="nsew")
    
        
if __name__ == "__main__":
    App("Class based app", (400, 400))