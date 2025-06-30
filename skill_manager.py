

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

    def update_exp_bar(self, current_exp, needed_exp, current_level, exp_constant = 5):
        if current_exp == needed_exp:
            current_level += 1
            current_exp = 0
            needed_exp = exp_constant * current_level
            #update level
        if current_exp < 0:
            if current_level > 1:
                current_level -= 1
                current_exp = (exp_constant * current_level)
                needed_exp = exp_constant * current_level

                #update level
        
        return current_exp, current_level, needed_exp
