from typing import Type

import pytest

from tests.formats.dataclass.cases import (
    attribute,
    attributes,
    element,
    elements,
    wildcard,
)
from xsdata.formats.dataclass.typing import (
    evaluate,
    evaluate_attribute,
    evaluate_attributes,
    evaluate_element,
    evaluate_elements,
    evaluate_wildcard,
)


def test_evaluate_with_typevar():
    result = evaluate(Type["str"], None)
    assert str == result

    with pytest.raises(TypeError):
        evaluate(Type, None)


@pytest.mark.parametrize("case,expected", attribute.tokens)
def test_evaluate_attribute_with_tokens(case, expected):
    if expected:
        assert expected == evaluate_attribute(case, tokens=True)
    else:
        with pytest.raises(TypeError):
            evaluate_attribute(case, tokens=True)


@pytest.mark.parametrize("case,expected", attribute.not_tokens)
def test_evaluate_attribute_without_tokens(case, expected):
    if expected:
        assert expected == evaluate_attribute(case, tokens=False)
    else:
        with pytest.raises(TypeError):
            evaluate_attribute(case, tokens=False)


@pytest.mark.parametrize("case,expected", attributes.cases)
def test_evaluate_attributes(case, expected):
    if expected:
        assert expected == evaluate_attributes(case)
    else:
        with pytest.raises(TypeError):
            evaluate_attributes(case)


@pytest.mark.parametrize("case,expected", element.tokens)
def test_evaluate_element_with_tokens(case, expected):
    if expected:
        assert expected == evaluate_element(case, tokens=True)
    else:
        with pytest.raises(TypeError):
            evaluate_element(case, tokens=True)


@pytest.mark.parametrize("case,expected", element.not_tokens)
def test_evaluate_element_without_tokens(case, expected):
    if expected:
        assert expected == evaluate_element(case, tokens=False)
    else:
        with pytest.raises(TypeError):
            evaluate_element(case, tokens=False)


@pytest.mark.parametrize("case,expected", elements.cases)
def test_evaluate_elements(case, expected):
    if expected:
        assert expected == evaluate_elements(case)
    else:
        with pytest.raises(TypeError):
            evaluate_elements(case)


@pytest.mark.parametrize("case,expected", wildcard.cases)
def test_evaluate_wildcard(case, expected):
    if expected:
        assert expected == evaluate_wildcard(case)
    else:
        with pytest.raises(TypeError):
            evaluate_wildcard(case)
