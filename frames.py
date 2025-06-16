import tkinter as tk
from tkinter import ttk
import random

class TopFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()
        self.pack(fill="x")

    def create_layout_and_widgets(self):
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(2, weight=2)

        name = tk.Label(self, text='Name:', background='red', anchor="w")
        total_level = tk.Label(self, text='Level:', background="purple", anchor="w")

        name.grid(column=0, sticky="nsew")
        total_level.grid(row = 0, column=1, sticky="nsew")


class MidFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()
        self.pack(expand=True, fill="both")

    def create_layout_and_widgets(self):
        self.skills_frame = tk.Frame(self) #frame ve kterém jsou skills
        self.skills_frame.pack(expand=True, fill="both")


class BottomFrame(ttk.Frame):
    def __init__(self, parent, skill_name_var, add_skill_callback): # 3 parameters, skill_name_var is there to go in the textvariable, in the App when called, it's the string_var
        super().__init__(parent)
        self.skill_name_var = skill_name_var
        self.add_skill_callback = add_skill_callback
        self.create_layout_and_widgets()
        self.pack(fill="x")

    def create_layout_and_widgets(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure((1, 2), weight=1, uniform="a")

        skill_name = ttk.Entry(self, textvariable=self.skill_name_var)
        add_skill_button = ttk.Button(self, text='Add skill', command=self.add_skill_callback)
        delete_mode_button = ttk.Button(self, text='Delete mode')  # placeholder

        skill_name.grid(column=0, sticky="nsew")
        add_skill_button.grid(row=0, column=1, sticky="nsew")
        delete_mode_button.grid(row=0, column=2, sticky="nsew")


class NewSkill(ttk.Frame):
    def __init__(self, parent, label_text, level, experience):
        super().__init__(parent)
        self.level = level
        self.experience = experience
        self.level_bar = None
        self.level_number = None
        self.experience_needed = 5 * self.level.get()
        self.color = f'#{random.randrange(256**3):06x}'
        self.create(label_text)
        self.pack(fill="x", pady=5)

        self.experience.trace_add("write", self.update_level_bar)

    def adding_exp(self):
        self.experience.set(self.experience.get() + 1)
        print(self.experience.get())
    
    def subtracting_exp(self):
        self.experience.set(self.experience.get() - 1)
        print(self.experience.get())

    def update_level_bar(self, *args):
        if self.level_bar:
            self.level_bar.config(
                text = f"XP {self.experience.get()}/{self.experience_needed}"
            )
        if self.experience.get() == self.experience_needed:
            self.level.set(self.level.get() + 1)
            self.experience.set(0)
            self.update_level()    

    def update_level(self, *args):
        self.experience_needed = 5 * self.level.get() #updates level and needed exp
        if self.level_number:
            self.level_number.config(
                text = f"Level: {self.level.get()}"

            )
            self.level_bar.config(
               text = f"XP{self.experience.get()}/{self.experience_needed}" 
            )

    def create(self, label_text):
        new_skill_frame = ttk.Frame(self, height=50, borderwidth=5, relief="solid")
        new_skill_frame.pack_propagate(False)
        new_skill_frame.pack(fill="x")

        new_skill_frame.columnconfigure(0, weight=3)
        new_skill_frame.columnconfigure(1, weight=2)
        new_skill_frame.columnconfigure((2, 3), weight=1, uniform="a")
        new_skill_frame.rowconfigure((0, 1), weight=1)

        skill_name = ttk.Label(new_skill_frame, text=label_text, anchor="w", borderwidth=1, relief="solid")
        self.level_number = ttk.Label(new_skill_frame, text=f"Level: {self.level.get()}", anchor="w", borderwidth=1, relief="solid")
        plus_button = ttk.Button(new_skill_frame, text="+", command = self.adding_exp)
        minus_button = ttk.Button(new_skill_frame, text="-", command = self.subtracting_exp)
        self.level_bar = tk.Label(new_skill_frame, text = f"XP{self.experience.get()}/{self.experience_needed}", anchor="center", borderwidth=2,relief="solid", background = self.color)


        skill_name.grid(row=0, column=0, sticky="nsew")
        self.level_number.grid(row=0, column=1, sticky="nsew")
        plus_button.grid(row=0, column=2, sticky="nsew")
        minus_button.grid(row=0, column=3, sticky="nsew")
        self.level_bar.grid(row=1, column=0, columnspan=4, sticky="nsew")
        
