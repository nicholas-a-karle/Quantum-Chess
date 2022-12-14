import numpy as np
from qiskit import *
from assets.globals import *
import pygame

class Gate:
    def __init__(self, type = EMPTY, target = EMPTY, control = EMPTY):
        self.type = type
        self.target = target
        self.control = control

    def clear(self):
        self.type = EMPTY
        self.target = EMPTY
        self.control = EMPTY

class CircuitGrid:

    def __init__(self, num_qbits, max_gates):
        self.num_qbits = num_qbits
        self.max_gates = max_gates
        self.gates = []
        for i in range(num_qbits):
            self.gates = self.gates + [Gate(EMPTY, i, EMPTY)]

    #clear gates (set all to empty) and therefore circuit
    def reset(self):
        for gate in self.gates:
            gate.clear()

    #return a qiskit QuantumCircuit object which the CircuitGrid represents
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
            
    def add_gate(self, type = EMPTY, target = EMPTY, control = EMPTY):
        for gate in self.gates:
            if gate.target == target:
                gate.type = type

#    def draw(self, surface):

    