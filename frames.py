import tkinter as tk
from tkinter import ttk, messagebox
import random
from skill_manager import SkillManager


class TopFrame(ttk.Frame):
    def __init__(self, parent, skills_list: dict, total_level: tk.IntVar, update_total_level_call):
        """                       ^list of all skills                        ^callback to label update function"""
        """Frame with character name and total level"""
        super().__init__(parent)
        self.skills = skills_list
        self.total_level = total_level
        self.update_total_level_text = update_total_level_call
        self.create_layout_and_widgets()

        self.total_level.trace_add("write", self.update_total_level_text)


    def create_layout_and_widgets(self):
        self.columnconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(2, weight=2)

        name = tk.Label(self, text='Name:', background='red', anchor="w")
        self.total_level_label = tk.Label(self, text=f'Level: {self.total_level.get()}', background="purple", anchor="w")

        name.grid(column=0, sticky="nsew")
        self.total_level_label.grid(row = 0, column=1, sticky="nsew")


class MidFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()

    def create_layout_and_widgets(self):
        self.skills_frame = tk.Frame(self) #frame ve kterém jsou skills
        self.skills_frame.pack(expand=True, fill="both")


class BottomFrame(ttk.Frame):
    def __init__(self, parent, skill_name_var: tk.StringVar, add_skill_callback): # 3 parameters, skill_name_var is there to go in the textvariable, in the App when called, it's the string_var
        super().__init__(parent)
        self.skill_name_var = skill_name_var
        self.add_skill_callback = add_skill_callback
        self.create_layout_and_widgets()

    def create_layout_and_widgets(self):
        self.columnconfigure(0, weight=2)
        self.columnconfigure((1, 2), weight=1, uniform="a")

        self.skill_name_entry = ttk.Entry(self, textvariable=self.skill_name_var)

        add_skill_button = ttk.Button(self, text='Add skill', command=self.add_skill_callback)
        delete_mode_button = ttk.Button(self, text='Delete mode') 

        self.skill_name_entry.grid(column=0, sticky="nsew")
        add_skill_button.grid(row=0, column=1, sticky="nsew")
        delete_mode_button.grid(row=0, column=2, sticky="nsew")

#sex
class NewSkill(ttk.Frame):
    """A frame representing a single skill with level and experience tracking."""

    NEEDED_EXP_CONSTANT = 5

    def __init__(self, parent, label_text: str, window_width: int, level: tk.IntVar, total_level: tk.IntVar, update_total_level_call):
        super().__init__(parent)
        self.skill_manager = SkillManager()
        self.experience = tk.IntVar(value = 0)
        self.level = level
        self.level_bar = None
        self.level_number = None
        self.experience_needed = self.NEEDED_EXP_CONSTANT * self.level.get()
        self.color = f'#{random.randrange(256**3):06x}'
        self.width = window_width
        self.total_level = total_level
        self.update_total_level_text = update_total_level_call
        self.create(label_text)
        self.pack(fill="x", pady=5)

        self.experience.trace_add("write", self.update_exp_bar)
        self.level.trace_add("write", self.update_total_level_text)


    def adding_exp(self):
        """Increase experience by 1."""
        self.experience.set(self.experience.get() + 1)
    
    def subtracting_exp(self):
        """Decrease experience by 1."""
        if self.level.get() == 1 and self.experience.get() == 0:
            messagebox.showwarning("Error", "Experience can't be any lower")
            return
        elif self.level.get() >= 1 and self.experience.get() >= 0:
            self.experience.set(self.experience.get() - 1)

    def update_exp_bar(self, *args):
        """Update the progress bar and handle level up/down."""
        
        # Logic handled in skill_manager
        experience_new, level_new, experience_needed_new = self.skill_manager.update_exp_bar(self.experience.get(), self.experience_needed, self.level.get())
        self.experience.set(experience_new)
        self.level.set(level_new)
        self.experience_needed = experience_needed_new

        # Error if level below zero
        if self.level.get() < 1:
            messagebox.showwarning("Error", "You are already at minimum level.")
            return
        
        # Update bar fill and XP text
        self.fill_width = int((self.bar_width / self.experience_needed) * self.experience.get()) if self.experience.get() > 0 else 0
        self.canvas_bar.coords(self.filled_part, 0, 0, self.fill_width, self.bar_height)

        if self.level_number:
            self.level_number.config(text = f"Level: {self.level.get()}")
            self.canvas_bar.itemconfigure(
                self.exp_bar, 
                text = f"XP {self.experience.get()}/{self.experience_needed}"
                )


    def create(self, label_text: tk.StringVar):
        """Creating the instance of NewSkill"""
        self.new_skill_frame = ttk.Frame(self, height=50, borderwidth=5, relief="solid")
        self.new_skill_frame.pack_propagate(False)
        self.new_skill_frame.pack(fill="x")

        self.new_skill_frame.columnconfigure(0, weight=3)
        self.new_skill_frame.columnconfigure(1, weight=2)
        self.new_skill_frame.columnconfigure((2, 3), weight=1, uniform="a")
        self.new_skill_frame.rowconfigure((0, 1), weight=1)

        self.skill_name = ttk.Label(self.new_skill_frame, text=label_text, anchor="w", borderwidth=1, relief="solid")
        self.level_number = ttk.Label(self.new_skill_frame, text=f"Level: {self.level.get()}", anchor="w", borderwidth=1, relief="solid")
        self.plus_button = ttk.Button(self.new_skill_frame, text="+", command = self.adding_exp)
        self.minus_button = ttk.Button(self.new_skill_frame, text="-", command = self.subtracting_exp)

        self.bar_width = self.width
        self.bar_height = 20
        
        # progress bar
        self.canvas_bar = tk.Canvas(self.new_skill_frame, width= self.bar_width, height= self.bar_height, bg="white", highlightthickness=0)
        self.canvas_bar.grid(row=1, columnspan = 4, sticky="ew")
        if self.experience.get() != 0:
            self.fill_width = int((self.bar_width/self.experience_needed)*self.experience.get()) #vyplněná část
        else:
            self.fill_width = 0
        self.canvas_bar.create_rectangle(0, 0, self.bar_width, self.bar_height, fill="#ddd")
        self.filled_part = self.canvas_bar.create_rectangle(0, 0, self.fill_width, self.bar_height, fill=self.color) 
        self.exp_bar = self.canvas_bar.create_text(self.bar_width//2, self.bar_height//2, text=f"XP{self.experience.get()}/{self.experience_needed}", fill="black")# text = to, co je teď na labelu dole

        self.skill_name.grid(row=0, column=0, sticky="nsew")
        self.level_number.grid(row=0, column=1, sticky="nsew")
        self.plus_button.grid(row=0, column=2, sticky="nsew")
        self.minus_button.grid(row=0, column=3, sticky="nsew")

        self.update_exp_bar