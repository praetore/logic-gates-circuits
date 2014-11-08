from utils import Consts
from utils.GateFactory import GateFactory

__author__ = 'Darryl'
__date__ = '3-11-2014'


def main():
    fac = GateFactory("Fac1")
    gates = [fac.create(Consts.AND) for i in range(1)] + \
            [fac.create(Consts.OR) for i in range(1)] + \
            [fac.create(Consts.XOR) for i in range(1)] + \
            [fac.create(Consts.NOR) for i in range(1)] + \
            [fac.create(Consts.XNOR) for i in range(1)] + \
            [fac.create(Consts.NOT) for i in range(1)]
    for i in range(len(gates)):
        print(gates[i].label)
        gates[i].performGateLogic()


if __name__ == '__main__':
    main()