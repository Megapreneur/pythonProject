import collections

c1 = collections.Counter("hello world")
print(c1)
c2 = collections.Counter("hi you")
print(c2)
c1.subtract(c2)
print(c1)

Person = collections.namedtuple("")