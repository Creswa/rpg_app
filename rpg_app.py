import tkinter as tk
from tkinter import messagebox
from frames import TopFrame, MidFrame, BottomFrame, NewSkill
from skill_manager import SkillManager


class App(tk.Tk):
    """Main application window for the RPG Skill Tracker."""
    def __init__(self, title: str, size: tuple[int, int]):
        super().__init__()

        # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        self.width = size[0]

        # Skill Manager
        self.skill_manager = SkillManager()

        # Shared variables
        self.new_skill_name = tk.StringVar(value="Enter new skill name")
        self.total_level = tk.IntVar(value = 0)
        self.skills = {} # List of all skills for further use 

        # Frames
        self.top_frame = TopFrame(self, self.skills, self.total_level, self.update_total_level_text)
        self.mid_frame = MidFrame(self)
        self.bottom_frame = BottomFrame(self, self.new_skill_name, self.create_new_skill)

        # Packing
        self.top_frame.pack(fill = "x")
        self.mid_frame.pack(expand=True, fill="both")
        self.bottom_frame.pack(fill="x")

    def create_new_skill(self):
        """Creation of new skill"""
        name = self.new_skill_name.get().strip()
        result = self.skill_manager.add_skill(name)
        if result == "empty":
            messagebox.showwarning("Input Error", "Skill name cannot be empty.")
            return
        if result == "long":
            messagebox.showwarning("Input Error", "Max 25 characters for skill name.")
            return
        if result == "duplicate":
            messagebox.showwarning("Duplicate Skill", "This skill is already added.")
            return
        level = tk.IntVar(value = 1)
        self.skills[name] = NewSkill(self.mid_frame.skills_frame, name, self.width, level,  self.total_level, self.update_total_level_text)
        self.update_total_level_text()  # Recalculate the sum of all levels)
        self.new_skill_name.set("") # Clear input


    def update_total_level_text(self, *args):
        """Updates the total level label in TopFrame"""
        total = sum(skill.level.get() for skill in self.skills.values())
        #total = self.skill_manager.sum_levels()
        self.total_level.set(total)
        self.top_frame.total_level_label.config(text=f"Level: {self.total_level.get()}")




if __name__ == "__main__":
    app = App("Class based app", (800, 800))
    app.mainloop()
