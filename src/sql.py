"""
SQL Class
"""

from itertools import product


class Sql:

    def __init__(self, left, right):
        """ """

        self.left = left
        self.right = right

        self.left_keys = sorted(set(list([i[0] for i in left])))
        self.right_keys = sorted(set(list([i[0] for i in right])))

    def inner_join(self):

        final = []
        for l in self.left:
            for r in self.right:

                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)

        return sorted(final)

    def left_join(self):

        final = []
        for l in self.left:
            for r in self.right:

                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)
                    continue

                elif r[0] not in self.left_keys:
                    continue

                elif l[0] != r[0]:
                    ser = l + (None, None)
                    final.append(ser)

                else:
                    raise ArithmeticError("Not possible")

        return sorted(list(set(final)))

    def right_join(self):

        final = []
        for r in self.right:
            for l in self.left:

                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)
                    continue

                elif l[0] not in self.right_keys:
                    continue

                elif l[0] != r[0]:
                    ser = (r[0],) + (None, None) + r[1:]
                    final.append(ser)

                else:
                    raise ArithmeticError("Not possible")

        return sorted(list(set(final)))

    def outter_join(self):

        final = []
        for l in self.left:
            for r in self.right:

                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)

                elif r[0] not in self.left_keys:
                    ser = (r[0],) + (None, None) + r[1:]
                    final.append(ser)

                elif l[0] != r[0]:
                    ser = l + (None, None)
                    final.append(ser)

                else:
                    raise ArithmeticError("Not possible")

        return sorted(list(set(final)))
