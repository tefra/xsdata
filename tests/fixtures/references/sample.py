from tests.fixtures.references.model import Child
from tests.fixtures.references.model import Parent
from tests.fixtures.references.model import Family

child1 = Child(name="albert", surname="fictional",age=7)
child2 = Child(name="bertha", surname="fictional", age=5)
parent = Parent(name="peter", surname="fictional", children=[child1,child2])
family = Family( member=[parent,child1,child2])