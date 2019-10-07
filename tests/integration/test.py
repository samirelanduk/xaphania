from unittest import TestCase
import xaphania

class Test(TestCase):

    def test(self):
        string = xaphania.ObjectType(name="String")
        integer = xaphania.ObjectType(name="Integer")

        query = xaphania.ObjectType(name="Query")
        person = xaphania.ObjectType(name="Person")

        query.add_field("leader", person)
        query.add_field(
         "person", person, arguments=[xaphania.Argument("id", integer)]
        )

        person.add_field("name", string)

        schema = xaphania.Schema(query)


        