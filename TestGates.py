from utils.GateFactory import GateFactory

__author__ = 'Darryl'
__date__ = '3-11-2014'


def main():
    fac = GateFactory("Fac1")
    gates = [fac.create("and") for i in range(1)] + \
            [fac.create("or") for i in range(1)] + \
            [fac.create("xor") for i in range(1)] + \
            [fac.create("xnor") for i in range(1)] + \
            [fac.create("nand") for i in range(1)] + \
            [fac.create("not") for i in range(1)]
    for i in range(len(gates)):
        print(gates[i].label)
        gates[i].performGateLogic()


if __name__ == '__main__':
    main()