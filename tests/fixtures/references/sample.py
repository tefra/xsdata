from tests.fixtures.references.model import OffSpring
from tests.fixtures.references.model import Parent
from tests.fixtures.references.model import Family

child1 = OffSpring(name="albert", surname="fictional", age=7)
child2 = OffSpring(name="bertha", surname="fictional", age=5)
parent = Parent(name="peter", surname="fictional", children=[child1, child2])
parent2 = Parent(name="penny",surname="fictional", children=[child1, child2])
parent3 =  Parent(name="deceased",surname="fictional", children=[child1, child2])
# note parent 1 references children that are not yet known (in XML terms) and  parent2 references children that have come before it
# and parent3 is a mix
family = Family( member=[parent,child1,parent3, child2, parent2], favorite=child1)