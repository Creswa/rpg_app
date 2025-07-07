import tkinter as tk
from tkinter import messagebox
from frames import TopFrame, MidFrame, BottomFrame, NewSkill
from skill_manager import SkillManager
import json

with open("skills.json", "r") as file:
    data = json.load(file)


class App(tk.Tk):
    """Main application window for the RPG Skill Tracker."""
    def __init__(self, title: str, size: tuple[int, int]):
        super().__init__()

        # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.width = size[0]
        
        # Loaded data
        self.data = data

        # Skill Manager
        self.skill_manager = SkillManager(self.data)

        # Shared variables
        self.new_skill_name = tk.StringVar(value="Enter new skill name")
        self.total_level = tk.IntVar(value = 0)

        # Frames
        self.top_frame = TopFrame(self, self.total_level, self.update_total_level_text)
        self.mid_frame = MidFrame(self)
        self.bottom_frame = BottomFrame(self, self.new_skill_name, self.create_new_skill, self.skill_manager)

        # Loading saved skills
        for x in data:
            name = x
            level_loaded = data[x]["level"]
            level = tk.IntVar()
            level.set(level_loaded)
            experience_loaded = data[x]["experience"]
            experience = tk.IntVar()
            experience.set(experience_loaded)
            self.load_skills(name, level, experience)
        self.update_total_level_text()
        
        # Packing
        self.top_frame.pack(fill = "x")
        self.mid_frame.pack(expand=True, fill="both")
        self.bottom_frame.pack(fill="x")
            
    def load_skills(self, name, level, experience):
        """Creates the skills based on save file"""
        NewSkill(self.mid_frame.skills_frame, name, self.width, level,  self.total_level, self.update_total_level_text, experience, self.data)
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            app.destroy()

    def create_new_skill(self):
        """Creation of new skill"""
        name = self.new_skill_name.get().strip()
        result = self.skill_manager.add_skill(name)
        experience = tk.IntVar(value = 0)
        level = tk.IntVar(value = 1)
        if result == "empty":
            messagebox.showwarning("Input Error", "Skill name cannot be empty.")
            return
        if result == "long":
            messagebox.showwarning("Input Error", "Max 25 characters for skill name.")
            return
        if result == "duplicate":
            messagebox.showwarning("Duplicate Skill", "This skill is already added.")
            return
        NewSkill(self.mid_frame.skills_frame, name, self.width, level,  self.total_level, self.update_total_level_text, experience, self.data)
        self.data[name] = {"level": level.get(), "experience": experience.get()}
        self.update_total_level_text()  # Recalculate the sum of all levels)
        self.new_skill_name.set("Enter name of a new skill") # Clear input
            

    def update_total_level_text(self, *args):
        """Updates the total level label in TopFrame"""
        total = sum(data[x]["level"] for x in self.data)
        self.total_level.set(total)
        self.top_frame.total_level_label.config(text=f"Level: {self.total_level.get()}")




if __name__ == "__main__":
    app = App("Class based app", (800, 800))
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
