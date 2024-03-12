"""
SQL Class
"""

from itertools import product
import logging


class Sql:

    def __init__(self, left, right):

        self.left = left
        self.right = right

    @property
    def left_keys(self):
        return sorted(set(list([i[0] for i in self.left])))

    @property
    def right_keys(self):
        return sorted(set(list([i[0] for i in self.right])))

    @property
    def candidates(self):

        return product(self.left, self.right)

    @property
    def inner_keys(self):

        keys = product(self.left_keys, self.right_keys)
        keys = [i[0] for i in keys if i[0] == i[1]]

        logging.info(f"inner_keys is {keys}")

        return sorted(list(set(keys)))

    @property
    def left_not_right(self):

        keys = product(self.left_keys, self.right_keys)
        keys = [i[0] for i in keys if i[0] not in self.right_keys]

        logging.info(f"left_not_right is {keys}")

        return sorted(list(set(keys)))

    @property
    def right_not_left(self):

        keys = product(self.left_keys, self.right_keys)
        keys = [i[1] for i in keys if i[1] not in self.left_keys]

        logging.info(f"right_not_left is {keys}")

        return sorted(list(set(keys)))

    def inner_join(self):

        final = []

        for left, right in self.candidates:
            if left[0] in self.inner_keys:
                final.append(left + right[1:])

        return sorted(set(list(final)))

    def left_join(self):

        final = []

        for left, right in self.candidates:

            if left[0] in self.inner_keys:
                final.append(left + right[1:])

            elif left[0] in self.left_not_right:
                final.append(left + (None, None))

        return sorted(set(list(final)))

    def right_join(self):

        final = []

        for left, right in self.candidates:

            if left[0] in self.inner_keys:
                final.append(left + right[1:])

            elif right[0] in self.right_not_left:
                final.append((right[0],) + (None, None) + right[1:])

        return sorted(list(set(final)))

    def outter_join(self):

        final = []
        for left, right in self.candidates:

            if left[0] in self.inner_keys:
                final.append(left + right[1:])

            elif right[0] in self.right_not_left:
                final.append((right[0],) + (None, None) + right[1:])

            elif left[0] in self.left_not_right:
                final.append(left + (None, None))

        return sorted(list(set(final)))
