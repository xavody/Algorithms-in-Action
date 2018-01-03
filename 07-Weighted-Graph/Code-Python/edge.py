"""
带权图的边
"""


class Edge:
    def __init__(self, a=None, b=None, weight=None):
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
