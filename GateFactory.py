from AndGate import AndGate
from OrGate import OrGate
from utils import profiled

__author__ = 'Darryl'
__date__ = '3-11-2014'


class GateFactory:
    def __init__(self, name):
        self.name = name

    @profiled
    def create(self, gatetype):
        name = "Gate %s from %s" % (GateFactory.create.called(), self.name)
        if gatetype == "and_gate":
            return AndGate(name)
        elif gatetype == "or_gate":
            return OrGate(name)