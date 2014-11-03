from abc import ABCMeta
from abstract.LogicGate import LogicGate
from utils.decorators import accept_binary_only

__author__ = 'Darryl'
__date__ = '3-11-2014'


class UnaryGate(LogicGate):
    __metaclass__ = ABCMeta

    def __init__(self, n):
        super().__init__(n)
        self.pin = None

    @accept_binary_only
    def getPin(self, questionstr=""):
        return super().getPin(questionstr)