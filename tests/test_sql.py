"""
Test the SQL module
"""

import logging
import os

import pytest

from src.sql import Sql
from src.vars import table_a, table_b


@pytest.fixture
def sql():
    """ """

    sql = Sql(table_a, table_b)

    return sql


class Ans:
    """Answer for the tests"""

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
        ("A", 1, 2, "1", "2"),
        ("A", 1, 2, "3", "4"),
        ("C", None, None, "1", "2"),
    ]

    outter = [
        ("A", 1, 2, "1", "2"),
        ("B", 1, 2, None, None),
        ("C", None, None, "1", "2"),
        ("A", 1, 2, "3", "4"),
    ]


class TestSQL:
    """Test the SQL module"""

    def test_init(self, sql):
        """ """

        assert sql.left == table_a
        assert sql.right == table_b
        assert sql.left_keys == ["A", "B"]
        assert sql.right_keys == ["A", "C"]

    def test_inner(self, sql):
        """ """

        ans = sql.inner_join()

        logging.warning(ans)

        assert len(ans) == len(Ans.inner)
        assert sorted(ans) == sorted(Ans.inner)

    def test_left(self, sql):
        """ """

        ans = sql.left_join()

        logging.warning(ans)

        assert len(ans) == len(Ans.left)
        assert sorted(ans) == sorted(Ans.left)

    def test_right(self, sql):
        """ """

        ans = sql.right_join()

        logging.warning(ans)

        assert len(ans) == len(Ans.right)
        assert sorted(ans) == sorted(Ans.right)

    def test_outter(self, sql):
        """ """

        ans = sql.outter_join()

        logging.warning(ans)

        assert len(ans) == len(Ans.outter)
        assert sorted(ans) == sorted(Ans.outter)
