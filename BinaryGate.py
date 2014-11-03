from abc import ABCMeta
from LogicGate import LogicGate
from utils import accept_binary_only

__author__ = 'Darryl'
__date__ = '3-11-2014'


class BinaryGate(LogicGate):
    __metaclass__ = ABCMeta

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    @accept_binary_only
    def getPinA(self):
        return super().getPin("Enter Pin A input for gate %s -->" % self.getLabel())

    @accept_binary_only
    def getPinB(self):
        return super().getPin("Enter Pin B input for gate %s -->" % self.getLabel())

    def getPin(self, questionstr=""):
        self.pinA = self.getPinA()
        self.pinB = self.getPinB()