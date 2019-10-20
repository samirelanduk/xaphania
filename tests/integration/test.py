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
        query.add_field(
         "people", person, list=True, arguments=[xaphania.Argument("age__gt", integer, required=False)]
        )

        schema = xaphania.Schema(query)


        string = xaphania.QueryString("{ user }")
        self.assertEqual(string.structure, {"user": None})
        string = xaphania.QueryString("{ user version }")
        self.assertEqual(string.structure, {"user": None, "version": None})
        string = xaphania.QueryString("{ user { name } version }")