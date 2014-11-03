from concrete.AndGate import AndGate
from concrete.NandGate import NandGate
from concrete.NorGate import NorGate
from concrete.NotGate import NotGate
from concrete.OrGate import OrGate
from concrete.XnorGate import XnorGate
from concrete.XorGate import XorGate
from utils.decorators import profiled

__author__ = 'Darryl'
__date__ = '3-11-2014'


class GateFactory:
    def __init__(self, name):
        self.name = name

    @profiled
    def create(self, gatetype):
        name = "Gate %s from %s" % (GateFactory.create.called(), self.name)
        if gatetype == "and":
            return AndGate(name)
        elif gatetype == "or":
            return OrGate(name)
        elif gatetype == "xor":
            return XorGate(name)
        elif gatetype == "not":
            return NotGate(name)
        elif gatetype == "xnor":
            return XnorGate(name)
        elif gatetype == "nand":
            return NandGate(name)
        elif gatetype == "nor":
            return NorGate(name)