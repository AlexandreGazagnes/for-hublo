"""
SQL Class
"""


class Sql:

    def __init__(self, left, right):
        """ """

        self.left = left
        self.right = right

        self.left_keys = [i[0] for i in left]
        self.right_keys = [i[0] for i in right]

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
                else:
                    ser = l + (None, None)
                    final.append(ser)

        return sorted(final)

    def right_join(self):
        pass

    def outter_join(self):
        pass
