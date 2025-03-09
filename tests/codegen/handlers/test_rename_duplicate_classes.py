from unittest import mock

from xsdata.codegen.container import ClassContainer
from xsdata.codegen.handlers import RenameDuplicateClasses
from xsdata.models.config import GeneratorConfig
from xsdata.models.enums import Tag
from xsdata.utils.testing import (
    AttrFactory,
    ClassFactory,
    FactoryTestCase,
)


class RenameDuplicateClassesTests(FactoryTestCase):
    def setUp(self) -> None:
        super().setUp()

        self.container = ClassContainer(config=GeneratorConfig())
        self.processor = RenameDuplicateClasses(container=self.container)

    def test_run_renames_classes_with_duplicate_qnames(self) -> None:
        classes = [
            ClassFactory.create(qname="{foo}A", tag=Tag.ELEMENT),
            ClassFactory.create(qname="{foo}a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_b", tag=Tag.ELEMENT),
            ClassFactory.create(qname="b", location="!@#$", tag=Tag.ELEMENT),
        ]
        self.container.extend(classes)
        self.processor.run()

        expected = {
            classes[0].ref: "{foo}A_1",
            classes[1].ref: "{foo}a_2",
            classes[3].ref: "_b_1",
            classes[4].ref: "b_2",
        }
        self.assertEqual(expected, self.processor.renames)
        self.assertEqual("{foo}A_1", classes[0].qname)
        self.assertEqual("{foo}a_2", classes[1].qname)
        self.assertEqual("_b_1", classes[3].qname)
        self.assertEqual("b_2", classes[4].qname)

    @mock.patch.object(RenameDuplicateClasses, "add_numeric_suffix")
    def test_rename_classes(self, mock_add_numeric_suffix) -> None:
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_A", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.processor.rename_classes(classes)
        self.processor.rename_classes(classes)

        mock_add_numeric_suffix.assert_has_calls(
            [
                mock.call(classes[1]),
                mock.call(classes[0]),
                mock.call(classes[2]),
                mock.call(classes[1]),
                mock.call(classes[0]),
                mock.call(classes[2]),
            ]
        )

    @mock.patch.object(RenameDuplicateClasses, "add_abstract_suffix")
    def test_rename_classes_with_abstract_type(self, mock_add_abstract_suffix) -> None:
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="_A", tag=Tag.ELEMENT, abstract=True),
        ]
        self.processor.rename_classes(classes)

        mock_add_abstract_suffix.assert_called_once_with(classes[1])

    @mock.patch.object(RenameDuplicateClasses, "add_numeric_suffix")
    def test_rename_classes_protects_single_element(self, mock_rename_class) -> None:
        classes = [
            ClassFactory.create(qname="_a", tag=Tag.ELEMENT),
            ClassFactory.create(qname="a", tag=Tag.COMPLEX_TYPE),
        ]
        self.processor.rename_classes(classes)

        mock_rename_class.assert_called_once_with(classes[1])

    def test_add_numeric_suffix_by_slug(self) -> None:
        target = ClassFactory.create(qname="{foo}_a")
        self.processor.container.add(target)
        self.processor.container.add(ClassFactory.create(qname="{foo}a_1"))
        self.processor.container.add(ClassFactory.create(qname="{foo}A_2"))
        self.processor.container.add(ClassFactory.create(qname="{bar}a_3"))
        self.processor.add_numeric_suffix(target)

        self.assertEqual("{foo}_a_3", target.qname)
        self.assertEqual("_a", target.meta_name)

        self.assertEqual([target], self.container.data["{foo}_a_3"])
        self.assertEqual([], self.container.data["{foo}_a"])
        self.assertEqual({target.ref: target.qname}, self.processor.renames)

    def test_add_numeric_suffix_by_name(self) -> None:
        target = ClassFactory.create(qname="{foo}_a")
        self.processor.use_names = True
        self.processor.container.add(target)
        self.processor.container.add(ClassFactory.create(qname="{bar}a_1"))
        self.processor.container.add(ClassFactory.create(qname="{thug}A_2"))
        self.processor.container.add(ClassFactory.create(qname="{bar}a_3"))
        self.processor.add_numeric_suffix(target)

        self.assertEqual("{foo}_a_4", target.qname)
        self.assertEqual("_a", target.meta_name)

        self.assertEqual([target], self.container.data["{foo}_a_4"])
        self.assertEqual([], self.container.data["{foo}_a"])
        self.assertEqual({target.ref: target.qname}, self.processor.renames)

    def test_add_abstract_suffix(self) -> None:
        target = ClassFactory.create(qname="{xsdata}line", abstract=True)
        self.processor.container.add(target)

        self.processor.add_abstract_suffix(target)

        self.assertEqual("{xsdata}line_abstract", target.qname)
        self.assertEqual("line", target.meta_name)
        self.assertEqual({target.ref: target.qname}, self.processor.renames)

    def test_update_references(self) -> None:
        target = ClassFactory.create()
        target.attrs.append(AttrFactory.reference(qname="foo", reference=1))
        target.attrs.append(
            AttrFactory.reference(
                qname="bar",
                reference=2,
            )
        )
        target.attrs[1].default = "@enum@bar::member"

        target.attrs.append(
            AttrFactory.reference(
                qname="thug",
                reference=3,
            )
        )

        self.processor.renames = {1: "bar", 2: "foo"}
        self.processor.update_references(target)

        self.assertEqual("bar", target.attrs[0].types[0].qname)
        self.assertEqual("foo", target.attrs[1].types[0].qname)
        self.assertEqual("@enum@foo::member", target.attrs[1].default)
        self.assertEqual("thug", target.attrs[2].types[0].qname)
