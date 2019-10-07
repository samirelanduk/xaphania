from unittest import TestCase
import xaphania

class Test(TestCase):

    def test(self):
        query = xaphania.ObjectType(name="Query")


        string = xaphania.ObjectType(name="String")
        integer = xaphania.ObjectType(name="Integer")

        
        person = xaphania.ObjectType(name="Person")
        person.add_field("name", string)
        person.add_field("age", integer, nullable=True)

        

        query.add_field("leader", person)
        query.add_field(
         "person", person, arguments=[xaphania.Argument("id", integer, required=True)]
        )

        print(query.schema_repr())
        print(person.schema_repr())
        schema = xaphania.Schema(query)


        