import datetime
import sys
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
    def assertCases(self, cases):
        for tp, result in cases.items():
            if result is False:
                with self.assertRaises(TypeError):
                    evaluate(tp)
            else:
                self.assertEqual(result, evaluate(tp), msg=tp)

    def test_evaluate_simple(self):
        types = (
            int,
            str,
            int,
            bool,
            float,
            bytes,
            object,
            datetime.time,
            datetime.date,
            datetime.datetime,
            XmlTime,
            XmlDate,
            XmlDateTime,
            XmlDuration,
            XmlPeriod,
            QName,
            Decimal,
            Enum,
            Namespace,
        )
        cases = {tp: (tp,) for tp in types}
        self.assertCases(cases)

    def test_evaluate_unsupported_typing(self):
        cases = [Any, Set[str]]

        for case in cases:
            with self.assertRaises(TypeError):
                evaluate(case)

    def test_evaluate_dict(self):
        cases = {
            Dict: (dict, str, str),
            Dict[str, int]: (dict, str, int),
            Dict[Any, Any]: False,
            Dict[Union[str, int], int]: False,
            Dict[int, Union[str, int]]: False,
            Dict[TypeVar("A", bound=int), str]: False,
            Dict[TypeVar("A"), str]: (dict, str, str),
        }

        if sys.version_info[:2] >= (3, 9):
            cases.update(
                {
                    dict: (dict, str, str),
                    dict[str, int]: (dict, str, int),
                    dict[Any, Any]: False,
                    dict[Union[str, int], int]: False,
                    dict[int, Union[str, int]]: False,
                    dict[TypeVar("A", bound=int), str]: False,
                    dict[TypeVar("A"), str]: (dict, str, str),
                }
            )

        if sys.version_info[:2] >= (3, 10):
            cases.update({dict[str | int, int]: False})

        self.assertCases(cases)

    def test_evaluate_list(self):
        A = TypeVar("A", int, str)

        cases = {
            List[A]: (list, int, str),
            List[int]: (list, int),
            List[Union[float, str]]: (list, float, str),
            List[Optional[int]]: (list, int),
            List[Tuple[int]]: (list, tuple, int),
            List[List[Union[bool, str]]]: (list, list, bool, str),
            List: (list, str),
            List[Dict[str, str]]: False,
            List[Any]: False,
        }

        if sys.version_info[:2] >= (3, 9):
            cases.update(
                {
                    list[A]: (list, int, str),
                    list[int]: (list, int),
                    list[Union[float, str]]: (list, float, str),
                    list[Optional[int]]: (list, int),
                    list[Tuple[int]]: (list, tuple, int),
                    list[list[Union[bool, str]]]: (list, list, bool, str),
                    list: (list, str),
                    list["str"]: (list, str),
                    list[dict[str, str]]: False,
                    list[Any]: False,
                }
            )

        self.assertCases(cases)

    def test_evaluate_tuple(self):
        A = TypeVar("A", int, str)

        cases = {
            Tuple[A]: (tuple, int, str),
            Tuple[int]: (tuple, int),
            Tuple[int, ...]: (tuple, int),
            Tuple[List[int], ...]: (tuple, list, int),
            Tuple[Union[float, str]]: (tuple, float, str),
            Tuple[Optional[int]]: (tuple, int),
            Tuple[Tuple[int]]: (tuple, tuple, int),
            Tuple[Tuple[Union[bool, str]]]: (tuple, tuple, bool, str),
            Tuple: (tuple, str),
            Tuple[Dict[str, str]]: False,
            Tuple[Any, ...]: False,
        }

        if sys.version_info[:2] >= (3, 9):
            cases.update(
                {
                    tuple[A]: (tuple, int, str),
                    tuple[int]: (tuple, int),
                    tuple[int, ...]: (tuple, int),
                    tuple[List[int], ...]: (tuple, list, int),
                    tuple[Union[float, str]]: (tuple, float, str),
                    tuple[Optional[int]]: (tuple, int),
                    tuple[tuple[int]]: (tuple, tuple, int),
                    tuple[tuple[Union[bool, str]]]: (tuple, tuple, bool, str),
                    tuple: (tuple, str),
                    tuple[dict[str, str]]: False,
                    tuple[Any, ...]: False,
                }
            )

        self.assertCases(cases)

    def test_evaluate_union(self):
        A = TypeVar("A", int, str)

        cases = {
            Optional[Union[bool, str]]: (bool, str),
            Optional[List[Union[int, float]]]: (list, int, float),
            Optional[A]: (int, str),
            Union[List[int], None]: (list, int),
            Union[List[int], List[str]]: False,
        }

        if sys.version_info[:2] >= (3, 10):
            cases.update(
                {
                    None | bool | str: (bool, str),
                    None | List[int | float]: (list, int, float),
                    None | A: (int, str),
                    List[int] | None: (list, int),
                    List[int] | List[str]: False,
                }
            )

        self.assertCases(cases)

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
