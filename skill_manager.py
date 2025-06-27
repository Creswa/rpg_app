

class SkillManager:
    def __init__(self):
        self.skills = {}
    
    def add_skill(self, name, level=1):
        if not name:
            return "empty"
        if len(name) > 25:
            return "long"
        if name in self.skills:
            return "duplicate"
        self.skills[name] = level
        return "ok"
    

    def sum_levels(self):
        total = sum(self.skills[x] for x in self.skills)
        return total

