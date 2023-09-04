"""Houses static unit tests for the models.py file."""

from typing import List

from project import models


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
