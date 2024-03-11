"""
SQL Class
"""


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

                # both
                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)

        return sorted(final)

    def left_join(self):

        final = []
        for l in self.left:
            for r in self.right:

                # both
                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)

                # right not in left
                elif r[0] not in self.left_keys:
                    pass

                # left not in right
                else:
                    ser = l + (None, None)
                    final.append(ser)

        return sorted(list(set(final)))

    def right_join(self):

        final = []
        for r in self.right:
            for l in self.left:

                # both
                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)
                    continue

                # left not in right
                elif l[0] not in self.right_keys:
                    continue

                # right not in left
                else:
                    ser = (r[0],) + (None, None) + r[1:]
                    final.append(ser)

        return sorted(list(set(final)))

    def outter_join(self):

        final = []
        for l in self.left:
            for r in self.right:

                # both
                if l[0] == r[0]:
                    ser = l + r[1:]
                    final.append(ser)

                # left not in right
                elif r[0] not in self.left_keys:
                    ser = (r[0],) + (None, None) + r[1:]
                    final.append(ser)

                # right not in left
                else:
                    ser = l + (None, None)
                    final.append(ser)

        return sorted(list(set(final)))
