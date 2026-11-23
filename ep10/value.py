import math

class Value:
    def __init__(self, data, children=()):
        self.data = data
        self.grad = 0.0
        self.children = children
        self.backward_step = lambda: None

    def __add__(self, other):
        out = Value(self.data + other.data, (self, other))
        def backward_step():
            self.grad += out.grad
            other.grad += out.grad
        out.backward_step = backward_step
        return out

    def __mul__(self, other):
        out = Value(self.data * other.data, (self, other))
        def backward_step():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out.backward_step = backward_step
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,))
        def backward_step():
            self.grad += (1 - t * t) * out.grad
        out.backward_step = backward_step
        return out

    def backward(self):
        order, seen = [], set()
        def visit(v):
            if v not in seen:
                seen.add(v)
                for child in v.children:
                    visit(child)
                order.append(v)
        visit(self)
        self.grad = 1.0
        for v in reversed(order):
            v.backward_step()
