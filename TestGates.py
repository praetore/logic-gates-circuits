from GateFactory import GateFactory

__author__ = 'Darryl'
__date__ = '3-11-2014'


def main():
    fac = GateFactory("Fac")
    gates = [fac.create("and_gate") for i in range(5)] + \
            [fac.create("or_gate") for i in range(5)]
    for i in range(len(gates)):
        print(gates[i].label)
        gates[i].getPin()
        if i == len(gates) - 1:
            [gates[x].performGateLogic() for x in range(len(gates))]


if __name__ == '__main__':
    main()