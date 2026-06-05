from Rational import Rational

class RationalList:
    def __init__(self, items=None):
        self._data = []
        if items:
            for item in items:
                self.append(item)

    def append(self, value):
        if not isinstance(value, Rational):
            value = Rational(value)
        self._data.append(value)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if not isinstance(value, Rational):
            value = Rational(value)
        self._data[index] = value

    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            for item in other._data:
                new_list.append(item)
        else:
            new_list.append(other)
        return new_list

    def __iadd__(self, other):
        if isinstance(other, RationalList):
            for item in other._data:
                self.append(item)
        else:
            self.append(other)
        return self

    def get_sum(self):
        total = Rational(0)
        for item in self._data:
            total = total + item
        return total
