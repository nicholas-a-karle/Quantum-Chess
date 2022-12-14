import numpy as np
from qiskit import *
from globals import *

class Gate:
    def __init__(self, type, target = -1, control = -1):
        self.type = type
        self.target = target
        self.control = control


class CircuitGrid:

    def __init__(self, num_qbits, max_gates):
        self.num_qbits = num_qbits
        self.max_gates = max_gates
        self.gates = [Gate(EMPTY)] * num_qbits * max_gates

    def construct_circuit(self):
        circ = QuantumCircuit(self.num_qbits)
        for gate in self.gates:
            target = gate.target
            control = gate.control
            type = gate.type

            #skip over where target is undefined
            if target == -1:
                continue

            #skip over empty
            if type == I_GATE:
                circ.i(target)
                #nonsene if controlled i, can ignore, should be error
            elif type == H_GATE:
                if (control is not EMPTY):
                    circ.ch(control, target)
                else:
                    circ.h(target)
            elif type == X_GATE:
                if (control is not EMPTY):
                    circ.cx(control, target)
                else:
                    circ.x(target)
            elif type == Y_GATE:
                if (control is not EMPTY):
                    circ.cy(control, target)
                else:
                    circ.y(target)
            elif type == Z_GATE:
                if (control is not EMPTY):
                    circ.cz(control, target)
                else:
                    circ.z(target)
            elif type == T_GATE:
                if (control is not EMPTY):
                    circ.ct(control, target)
                else:
                    circ.t(target)
            


    