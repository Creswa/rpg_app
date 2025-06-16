import tkinter as tk
from tkinter import ttk

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
    def __init__(self, parent, label_text):
        super().__init__(parent)
        self.create(label_text)
        self.pack(fill="x", pady=5)

    def create(self, label_text):
        new_skill_frame = ttk.Frame(self, height=50, borderwidth=5, relief="solid")
        new_skill_frame.pack_propagate(False)
        new_skill_frame.pack(fill="x")

        new_skill_frame.columnconfigure((0, 1), weight=2)
        new_skill_frame.columnconfigure((2, 3), weight=1, uniform="a")
        new_skill_frame.rowconfigure((0, 1), weight=1)

        skill_name = ttk.Label(new_skill_frame, text=label_text, anchor="w", borderwidth=1, relief="solid")
        level = ttk.Label(new_skill_frame, text="Level", anchor="w", borderwidth=1, relief="solid")
        minus_button = ttk.Button(new_skill_frame, text="-")
        plus_button = ttk.Button(new_skill_frame, text="+")
        level_bar = tk.Label(new_skill_frame, text="Level progress", anchor="center", borderwidth=2,relief="solid", background="red")

        skill_name.grid(row=0, column=0, sticky="nsew")
        level.grid(row=0, column=1, sticky="nsew")
        minus_button.grid(row=0, column=2, sticky="nsew")
        plus_button.grid(row=0, column=3, sticky="nsew")
        level_bar.grid(row=1, column=0, columnspan=4, sticky="nsew")
