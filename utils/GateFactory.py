from concrete.AndGate import AndGate
from concrete.NandGate import NandGate
from concrete.NorGate import NorGate
from concrete.NotGate import NotGate
from concrete.OrGate import OrGate
from concrete.XnorGate import XnorGate
from concrete.XorGate import XorGate
from utils.Consts import AND, OR, XOR, NOT, XNOR, NAND, NOR
from utils.decorators import profiled



__author__ = 'Darryl'
__date__ = '3-11-2014'


class GateFactory:
    def __init__(self, name):
        self.name = name

    @profiled
    def create(self, gatetype):
        name = "Gate %s from %s" % (GateFactory.create.called(), self.name)
        if gatetype == AND:
            return AndGate(name)
        elif gatetype == OR:
            return OrGate(name)
        elif gatetype == XOR:
            return XorGate(name)
        elif gatetype == NOT:
            return NotGate(name)
        elif gatetype == XNOR:
            return XnorGate(name)
        elif gatetype == NAND:
            return NandGate(name)
        elif gatetype == NOR:
            return NorGate(name)