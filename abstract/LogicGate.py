from abc import abstractmethod, ABCMeta

__author__ = 'Darryl'
__date__ = '3-11-2014'


class LogicGate:
    __metaclass__ = ABCMeta

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

    @abstractmethod
    def performGateLogic(self):
        pass

    @abstractmethod
    def getPin(self, questionstr=""):
        if not questionstr:
            questionstr = "Enter Pin input for gate %s -->" % self.getLabel()
        return input(questionstr)