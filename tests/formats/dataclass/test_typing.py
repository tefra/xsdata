import datetime
from decimal import Decimal
from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from unittest import TestCase
from xml.etree.ElementTree import QName

from xsdata.formats.bindings import T
from xsdata.formats.dataclass.typing import evaluate
from xsdata.formats.dataclass.typing import get_args
from xsdata.formats.dataclass.typing import get_origin
from xsdata.models.datatype import XmlDate
from xsdata.models.datatype import XmlDateTime
from xsdata.models.datatype import XmlDuration
from xsdata.models.datatype import XmlPeriod
from xsdata.models.datatype import XmlTime
from xsdata.models.enums import Namespace


class TypingTests(TestCase):
    def test_get_origin_list(self):
        self.assertEqual(List, get_origin(List[int]))
        self.assertEqual(List, get_origin(List[Union[int]]))

        with self.assertRaises(TypeError):
            get_origin(List)

    def test_get_origin_dict(self):
        self.assertEqual(Dict, get_origin(Dict))
        self.assertEqual(Dict, get_origin(Dict[int, str]))
        self.assertEqual(Dict, get_origin(Dict[Union[int], Union[str]]))

    def test_get_origin_union(self):
        self.assertIsNone(get_origin(Union[int]))
        self.assertEqual(Union, get_origin(Optional[int]))
        self.assertEqual(Union, get_origin(Union[int, str]))

        with self.assertRaises(TypeError):
            get_origin(Union)

        with self.assertRaises(TypeError):
            get_origin(Optional)

    def test_get_origin_type(self):
        self.assertEqual(Type, get_origin(Type[str]))

    def test_get_origin_types(self):
        self.assertIsNone(get_origin(str))
        self.assertIsNone(get_origin(int))
        self.assertIsNone(get_origin(bool))
        self.assertIsNone(get_origin(float))
        self.assertIsNone(get_origin(bytes))
        self.assertIsNone(get_origin(object))
        self.assertIsNone(get_origin(datetime.time))
        self.assertIsNone(get_origin(datetime.date))
        self.assertIsNone(get_origin(datetime.datetime))
        self.assertIsNone(get_origin(XmlTime))
        self.assertIsNone(get_origin(XmlDate))
        self.assertIsNone(get_origin(XmlDateTime))
        self.assertIsNone(get_origin(XmlDuration))
        self.assertIsNone(get_origin(XmlPeriod))
        self.assertIsNone(get_origin(QName))
        self.assertIsNone(get_origin(Decimal))
        self.assertIsNone(get_origin(Enum))
        self.assertIsNone(get_origin(Namespace))

    def test_get_origin_unsupported(self):
        unsupported = [Set, Tuple]
        for check in unsupported:
            with self.assertRaises(TypeError, msg=check):
                get_origin(check)

    def test_get_args(self):
        self.assertEqual((), get_args(int))
        self.assertEqual((int,), get_args(List[int]))
        self.assertEqual((List[int], type(None)), get_args(Optional[List[int]]))
        self.assertEqual((int, str), get_args(Union[int, str]))
        self.assertEqual((int, type(None)), get_args(Optional[int]))
        self.assertEqual((int, type(None), str), get_args(Union[Optional[int], str]))

    def test_evaluate_simple(self):
        self.assertEqual((int,), evaluate(int))

    def test_evaluate_dict(self):
        self.assertEqual((dict, str, str), evaluate(Dict))
        self.assertEqual((dict, str, int), evaluate(Dict[str, int]))

        unsupported_cases = [
            Dict[Any, Any],
            Dict[Union[str, int], int],
            Dict[int, Union[str, int]],
            Dict[TypeVar("A", bound=int), str],
        ]

        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_union(self):
        self.assertEqual((bool, str), evaluate(Optional[Union[bool, str]]))
        self.assertEqual(
            (list, int, float), evaluate(Optional[List[Union[int, float]]])
        )

        unsupported_cases = [Optional[T], Union[List[int], Dict[str, str]]]
        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_list(self):
        A = TypeVar("A", int, str)

        self.assertEqual((list, int, str), evaluate(List[A]))
        self.assertEqual((list, int), evaluate(List[int]))
        self.assertEqual((list, float, str), evaluate(List[Union[float, str]]))
        self.assertEqual((list, int), evaluate(List[Optional[int]]))
        self.assertEqual(
            (list, list, bool, str), evaluate(List[List[Union[bool, str]]])
        )

        unsupported_cases = [List, List[Dict[str, str]]]
        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_type(self):
        self.assertEqual((str,), evaluate(Type["str"]))

        with self.assertRaises(TypeError):
            evaluate(Type)

    def test_evaluate_typevar(self):
        A = TypeVar("A", int, str)
        B = TypeVar("B", bound=object)

        self.assertEqual((int, str), evaluate(A))
        self.assertEqual((object,), evaluate(B))

        with self.assertRaises(TypeError):
            evaluate(T)
