from abstract.BinaryGate import BinaryGate
from utils.decorators import convert_boolean_to_binary

__author__ = 'Darryl'
__date__ = '3-11-2014'


class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    @convert_boolean_to_binary
    def performGateLogic(self):
        self.getPin()
        return self.pinA != self.pinB or self.pinA == 1 and self.pinB == 1