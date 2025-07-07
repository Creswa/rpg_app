import json

class SkillManager:
    def __init__(self, data):
        self.data = data
    def add_skill(self, name, level=1):
        if not name or name == "Enter name of a new skill":
            return "empty"
        if len(name) > 25:
            return "long"
        if name in self.data:
            return "duplicate"
        return "ok"

    def update_exp_bar(self, current_exp, needed_exp, current_level, exp_constant = 5):
        if current_exp == needed_exp:
            current_level += 1
            current_exp = 0
            needed_exp = exp_constant * current_level
        if current_exp < 0:
            if current_level > 1:
                current_level -= 1
                current_exp = (exp_constant * current_level)
                needed_exp = exp_constant * current_level
        return current_exp, current_level, needed_exp

    def save_data(self):
        with open("skills.json", "w") as file:
            json.dump(self.data, file, indent = 4)