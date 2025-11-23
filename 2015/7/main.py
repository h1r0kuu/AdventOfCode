separator = " -> "
from operator import *
operators = {"AND": and_, "OR": or_, "LSHIFT": lshift, "RSHIFT": rshift, "NOT": inv}

wires = {}
for line in open(0):
    splitted = line.split()
    if splitted[0] == 'NOT':
        wires[splitted[-1]] = wires[splitted[1]]
        wires[splitted[1]] = 0
    
