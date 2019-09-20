class ObjectType:
    
    def __init__(self, name):
        self.name = name
        self.fields = []
    

    def __repr__(self):
        return f"<{self.name} Type>"
    

    def add_field(self, field_name, object_type):
        self.fields.append(Field(field_name, object_type))



class Field:
    
    def __init__(self, name, object_type):
        self.name = name
        self.type = object_type
    

    def __repr__(self):
        return f"<{self.name} Field ({self.type.name})>"



