from tests.fixtures.references.model import Child
from tests.fixtures.references.model import Parent
from tests.fixtures.references.model import Family

child1 = Child(name="albert", age=7)
child2 = Child(name="bertha", age=5)
parent = Parent(name="peter", children=[child1,child2])
family = Family(surname="fictional", member=[parent,child1,child2])