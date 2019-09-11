from unittest import TestCase
import xaphania

class Test(TestCase):

    def test(self):
        string = xaphania.ObjectType(name="String")


        query = xaphania.ObjectType(
         name="Query",
         fields=[
          xaphania.Field(name="version", type=string)
         ]
        )