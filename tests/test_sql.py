"""
Test the SQL module
"""

import pytest

from src.sql import Sql
from src.vars import table_a, table_b


class Ans:
    inner = [
        ("A", 1, 2, "1", "2"),
        ("A", 1, 2, "3", "4"),
    ]

    left = [
        ("A", 1, 2, "1", "2"),
        ("B", 1, 2, None, None),
        ("A", 1, 2, "3", "4"),
    ]

    right = [
        ("A", "1", "2", 1, 2),
        ("C", "1", "2", None, None),
        ("A", "3", "4", 1, 2),
    ]

    outter = [
        ("A", 1, 2, "1", "2"),
        ("B", 1, 2, None, None),
        ("C", None, None, "1", "2"),
        ("A", 1, 2, "3", "4"),
    ]


class TestSQL:

    def test_inner(table_a, table_b):

        assert Sql.inner_join(table_a, table_b) == Ans.inner

    def test_outter(table_a, table_b):
        """ """

        assert Sql.ou == left(table_a, table_b)

    def test_left(table_a, table_b):
        pass

    def test_right(table_a, table_b):
        pass
