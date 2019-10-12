class ObjectType:
    
    def __init__(self, name):
        self.name = name
        self.fields = []
    

    def __repr__(self):
        return f"<{self.name} Type>"
    

    def add_field(self, *args, **kwargs):
        self.fields.append(Field(*args, **kwargs))
    

    def schema_repr(self):
        return "type {} {{\n  {}\n}}".format(
         self.name,
         "\n  ".join(f.schema_repr() for f in self.fields)
        )



class Field:
    
    def __init__(self, name, object_type, arguments=None, list=False, nullable=False):
        self.name = name
        self.type = object_type
        self.arguments = arguments or []
        self.nullable = nullable
        self.list = list
    

    def __repr__(self):
        return f"<{self.name} Field ({self.type.name})>"

    
    def schema_repr(self):
        return "{}{}: {}{}{}{}".format(
         self.name,
         "" if not self.arguments else\
          f"({', '.join(a.schema_repr() for a in self.arguments)})",
         "[" if self.list else "",
         self.type.name, "]" if self.list else "",
         "" if self.nullable else "!",
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



