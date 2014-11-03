from functools import wraps
import types
from AndGate import AndGate
from OrGate import OrGate

__author__ = 'Darryl'
__date__ = '3-11-2014'


class CreationProfiler:
    def __init__(self, func):
        wraps(func)(self)
        self.called = 0

    def __call__(self, *args, **kwargs):
        self.called += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


class GateFactory:
    def __init__(self, name):
        self.name = name

    @CreationProfiler
    def create(self, gatetype):
        name = "Gate %s from %s" % (GateFactory.create.called, self.name)
        if gatetype == "and_gate":
            return AndGate(name)
        elif gatetype == "or_gate":
            return OrGate(name)


if __name__ == '__main__':
    fac = GateFactory("Fac")
    gates = [fac.create("and_gate") for i in range(10)]
    for i in range(len(gates)):
        print(gates[i].label)
        gates[i].getPin()


