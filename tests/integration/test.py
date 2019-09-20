from unittest import TestCase
import xaphania

class Test(TestCase):

    def test(self):
        string = xaphania.ObjectType(name="String")

        query = xaphania.ObjectType(name="Query")
        person = xaphania.ObjectType(name="Person")

        query.add_field("leader", person)

        person.add_field("name", string)

        