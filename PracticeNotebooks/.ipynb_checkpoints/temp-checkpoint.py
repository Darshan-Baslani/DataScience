import math

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label
        self._backward = lambda: None
        
    def __repr__(self):
        return f"Value(data={self.data})"
        
    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')

        def _backward():
            self.grad += 1.0 * out.grad
            other.grad += 1.0 * out.grad
        out._backward = _backward

        return out         

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other) 

    def __neg__(self):
        return self * -1
        
    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (other**-1)

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "Int and Float only"
        out = Value(self.data ** other, (self, ), f"{self.data}**{other}")

        def _backward():
            self.grad += other * (self.data ** (other-1)) * out.grad
        out._backward = _backward
        return out

    def exp(self):
        x = self.data
        out = Value(math.exp(x), (self, ), 'exp')

        def _backward():
            self.grad += out.data * out.grad
        out._backward = _backward
        return out

    def tanh(self):
        x = self.data
        tanh = (math.exp(2 * x) - 1) / (math.exp(2 * x) + 1)
        out = Value(tanh, (self, ), "tanh")

        def _backward():
            self.grad += (1 - tanh**2) * out.grad
        out._backward = _backward        
        return out

    def backward(self):      
        topo = []
        visited = set()
        
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        self.grad = 1.0
        build_topo(self)        
        for node in reversed(topo):
            node._backward()

# Forward Propagation
x1 = Value(2.0, label="x1")
x2 = Value(1.0, label="x2")

w1 = Value(-1.0, label="w1")
w2 = Value(2.0, label="w2")

b = Value(1.5, label="b")

x1w1 = x1 * w1; x1w1.label = "x1w1"
x2w2 = x2 * w2; x2w2.label = "x2w2"
x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = "x1w1 + x2w2"

n = x1w1x2w2 + b; n.label = "n"

e = (2 * n).exp()
o = (e - 1) / (e + 1)
o.backward()

print(f"x1.grad: {x1.grad}")
print(f"x2.grad: {x2.grad}")
print(f"w1.grad: {w1.grad}")
print(f"w2.grad: {w2.grad}")
print(f"b.grad: {b.grad}")
