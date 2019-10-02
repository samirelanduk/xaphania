class ObjectType:
    
    def __init__(self, name):
        self.name = name
        self.fields = []
    

    def __repr__(self):
        return f"<{self.name} Type>"
    

    def add_field(self, field_name, object_type, arguments=None):
        arguments = arguments or []
        self.fields.append(Field(field_name, object_type, arguments))



class Field:
    
    def __init__(self, name, object_type, arguments):
        self.name = name
        self.type = object_type
        self.arguments = arguments
    

    def __repr__(self):
        return f"<{self.name} Field ({self.type.name})>"



class Argument:

    def __init__(self, name, object_type, required=False):
        self.name = name
        self.type = object_type
        self.required = required
    

    def __repr__(self):
        return "<{} {} argument ({}required)>".format(
         self.name, self.type.name, "" if self.required else "not "
        )



