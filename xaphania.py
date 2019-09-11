class ObjectType:
    
    def __init__(self, name, fields=None):
        self.name = name
        self.fields = fields or []
    

    def __repr__(self):
        return f"<{self.name} Type>"



class Field:
    
    def __init__(self, name, type):
        self.name = name
        self.type = type
    

    def __repr__(self):
        return f"<{self.name} Field ({self.type.name})>"



