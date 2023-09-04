"""Houses dynamic unit tests for the models.py file."""

import inspect
from typing import List

import pytest

from project import models


def is_builtin_data_structure_or_type(obj: object) -> bool:
    """Return True if obj is a builtin data structure or type."""
    return isinstance(obj, (list, dict, set, tuple, bool, bytes, float, int, str))


def test_all_models_have_unit_tests() -> None:
    """Unit test that validates test coverage for models."""
    model_objects = inspect.getmembers(models, is_builtin_data_structure_or_type)
    for model_object, _ in model_objects:
        if model_object.startswith("__"):
            print(f"Ignoring magic method or attribute {model_object}")
            continue
        test_name = f"test_{model_object}"
        for global_object in globals():
            if test_name in global_object:
                break
        else:
            pytest.fail(f"Missing unit test for model {model_object}.")


def generic_list_of_strings_test(list_of_strings: List[str]) -> None:
    """Tests whether a supposed list of strings is as described."""
    assert isinstance(list_of_strings, list)
    assert len(list_of_strings) > 0
    for item in list_of_strings:
        assert isinstance(item, str)


def test_NETWORK_VRFS() -> None:
    """Ensure that the NETWORK_VRFS model is a list of strings."""
    generic_list_of_strings_test(models.NETWORK_VRFS)


def test_IPV4_SUBNETS() -> None:
    """Ensure that the IPV4_SUBNETS model is a list of strings."""
    generic_list_of_strings_test(models.IPV4_SUBNETS)


def test_IPV6_SUBNETS() -> None:
    """Ensure that the IPV6_SUBNETS model is a list of strings."""
    generic_list_of_strings_test(models.IPV6_SUBNETS)
