"""
带权图的边
"""


class Edge:
    def __init__(self, a, b, weight):
        self.a = a
        self.b = b
        self.weight = weight

    def get_v(self):
        """返回第一个顶点"""
        return self.a

    def get_w(self):
        """返回第二个顶点"""
        return self.b

    def get_weight(self):
        """返回权值"""
        return self.weight

    def other(self, x):
        """给定一个顶点, 返回另一个顶点"""
        assert x == self.a or x == self.b
        return self.a if x == self.b else self.b

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __str__(self):
        return '' + str(self.a) + '-' + str(self.b) + ': ' + str(self.weight)
