from BinaryGate import BinaryGate
from utils import convert_boolean_to_binary

__author__ = 'Darryl'
__date__ = '3-11-2014'


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    @convert_boolean_to_binary
    def performGateLogic(self):
        self.getPin()
        return self.pinA == 1 and self.pinB == 1

if __name__ == '__main__':
    g1 = AndGate("G1")
    print(g1.getOutput())