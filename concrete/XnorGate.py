from abstract.BinaryGate import BinaryGate
from utils.decorators import convert_boolean_to_binary

__author__ = 'Darryl'
__date__ = '3-11-2014'


class XnorGate(BinaryGate):
    @convert_boolean_to_binary
    def performGateLogic(self):
        self.getPin()
        return self.pinB == self.pinA