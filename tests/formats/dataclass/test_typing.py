import datetime
import sys
from decimal import Decimal
from enum import Enum
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
from typing import Type
from typing import TypeVar
from typing import Union
from unittest import TestCase
from xml.etree.ElementTree import QName

import typing_extensions

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

    def test_evaluate_simple(self):
        self.assertEqual((int,), evaluate(int))

    def test_evaluate_dict(self):
        self.assertEqual((dict, str, str), evaluate(Dict))
        self.assertEqual((dict, str, int), evaluate(Dict[str, int]))

        if sys.version_info > (3, 10):
            self.assertEqual((dict, str, str), evaluate(dict))
            self.assertEqual((dict, str, int), evaluate(dict[str, int]))

        unsupported_cases = [
            Dict[Any, Any],
            Dict[Union[str, int], int],
            Dict[int, Union[str, int]],
            Dict[TypeVar("A", bound=int), str],
        ]

        if sys.version_info > (3, 10):
            unsupported_cases.extend(
                [
                    dict[Any, Any],
                    dict[str | int, int],
                    dict[int, str | int],
                    dict[TypeVar("A", bound=int), str],
                ]
            )

        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_union(self):
        self.assertEqual((bool, str), evaluate(Optional[Union[bool, str]]))
        self.assertEqual(
            (list, int, float), evaluate(Optional[List[Union[int, float]]])
        )

        if sys.version_info >= (3, 10):
            self.assertEqual((bool, str), evaluate(bool | str | None))
            self.assertEqual((list, int, float), evaluate(list[int | float], None))

        unsupported_cases = [Optional[T], Union[List[int], Dict[str, str]]]
        if sys.version_info > (3, 10):
            unsupported_cases.extend([T | None, list[int] | dict[str, str]])

        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_list(self):
        A = TypeVar("A", int, str)

        self.assertEqual((list, int, str), evaluate(List[A]))
        self.assertEqual((list, int), evaluate(List[int]))
        self.assertEqual((list, float, str), evaluate(List[Union[float, str]]))
        self.assertEqual((list, int), evaluate(List[Optional[int]]))
        self.assertEqual((list, tuple, int), evaluate(List[Tuple[int]]))
        self.assertEqual(
            (list, list, bool, str), evaluate(List[List[Union[bool, str]]])
        )

        unsupported_cases = [List, List[Dict[str, str]]]
        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_tuple(self):
        A = TypeVar("A", int, str)

        self.assertEqual((tuple, int, str), evaluate(Tuple[A]))
        self.assertEqual((tuple, int), evaluate(Tuple[int]))
        self.assertEqual((tuple, int), evaluate(Tuple[int, ...]))
        self.assertEqual((tuple, list, int), evaluate(Tuple[List[int], ...]))
        self.assertEqual((tuple, float, str), evaluate(Tuple[Union[float, str]]))
        self.assertEqual((tuple, int), evaluate(Tuple[Optional[int]]))
        self.assertEqual(
            (tuple, tuple, bool, str), evaluate(Tuple[Tuple[Union[bool, str]]])
        )

        if sys.version_info > (3, 10):
            self.assertEqual((tuple, int, str), evaluate(tuple[A]))
            self.assertEqual((tuple, int), evaluate(tuple[int]))
            self.assertEqual((tuple, int), evaluate(tuple[int, ...]))
            self.assertEqual((tuple, list, int), evaluate(tuple[list[int], ...]))
            self.assertEqual((tuple, float, str), evaluate(tuple[float | str]))
            self.assertEqual((tuple, int), evaluate(tuple[Optional[int]]))
            self.assertEqual(
                (tuple, tuple, bool, str), evaluate(tuple[tuple[bool | str]])
            )

        unsupported_cases = [Tuple, Tuple[Dict[str, str]]]
        if sys.version_info > (3, 10):
            unsupported_cases.extend([tuple[dict[str, str]]])

        for case in unsupported_cases:
            with self.assertRaises(TypeError, msg=case):
                evaluate(case)

    def test_evaluate_type(self):
        self.assertEqual((str,), evaluate(Type["str"]))

        if sys.version_info > (3, 10):
            self.assertEqual((str,), evaluate(type["str"]))

        with self.assertRaises(TypeError):
            evaluate(Type)

    def test_evaluate_typevar(self):
        A = TypeVar("A", int, str)
        B = TypeVar("B", bound=object)

        self.assertEqual((int, str), evaluate(A))
        self.assertEqual((object,), evaluate(B))

        with self.assertRaises(TypeError):
            evaluate(T)
