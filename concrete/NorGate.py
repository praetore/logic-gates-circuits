from abstract.BinaryGate import BinaryGate
from utils.decorators import convert_boolean_to_binary

__author__ = 'Darryl'
__date__ = '3-11-2014'


class NorGate(BinaryGate):
    @convert_boolean_to_binary
    def performGateLogic(self):
        return self.pinA == 0 and self.pinA == 0