from abstract.UnaryGate import UnaryGate
from utils.decorators import convert_boolean_to_binary

__author__ = 'Darryl'
__date__ = '3-11-2014'


class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    @convert_boolean_to_binary
    def performGateLogic(self):
        self.getPin()
        return self.pin == 0