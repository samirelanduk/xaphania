class ObjectType:
    
    def __init__(self, name):
        self.name = name
        self.fields = []
    

    def __repr__(self):
        return f"<{self.name} Type>"
    

    def add_field(self, field_name, object_type, arguments=None, nullable=False):
        arguments = arguments or []
        self.fields.append(Field(field_name, object_type, arguments, nullable))
    

    def schema_repr(self):
        return "type {} {{\n  {}\n}}".format(
         self.name,
         "\n  ".join(f.schema_repr() for f in self.fields)
        )



class Field:
    
    def __init__(self, name, object_type, arguments, nullable=False):
        self.name = name
        self.type = object_type
        self.arguments = arguments
        self.nullable = nullable
    

    def __repr__(self):
        return f"<{self.name} Field ({self.type.name})>"

    
    def schema_repr(self):
        return "{}{}: {}{}".format(
         self.name,
         "" if not self.arguments else\
          f"({', '.join(a.schema_repr() for a in self.arguments)})",
         self.type.name, "" if self.nullable else "!"
        )



class Argument:

    def __init__(self, name, object_type, required=False):
        self.name = name
        self.type = object_type
        self.required = required
    

    def __repr__(self):
        return "<{} {} argument ({}required)>".format(
         self.name, self.type.name, "" if self.required else "not "
        )
    

    def schema_repr(self):
        return "{}: {}{}".format(
         self.name, self.type.name, "!" if self.required else ""
        )



class Schema:

    def __init__(self, query):
        self.query = query
    

    def __repr__(self):
        return "<Schema>"



