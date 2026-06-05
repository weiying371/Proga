from Rational import Rational

class Rational_list:
    def __init__(self, items=None):
        self._data = []
        if items is not None:
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

    def __iadd__(self, other):
        if isinstance(other, Rational_list):
            for item in other._data:
                self.append(item)
        else:
            self.append(other)
        return self

    def __iter__(self):
        sorted_data = sorted(
            self._data,
            key=lambda x: (x["d"], x["n"]),
            reverse=True
        )
        return iter(sorted_data)

    def get_sum(self):
        total = Rational(0)
        for item in self._data:
            total = total + item
        return total
