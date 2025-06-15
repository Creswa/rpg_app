import json

class New_skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        # ... plus maybe some widgets (not JSON-compatible)

def to_dict(self):
    return {
        "name": self.name,
