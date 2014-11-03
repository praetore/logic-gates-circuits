from LogicGate import LogicGate
from utils import accept_binary_only

__author__ = 'Darryl'
__date__ = '3-11-2014'


class UnaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    @accept_binary_only
    def getPin(self, questionstr=""):
        return super().getPin(questionstr)

