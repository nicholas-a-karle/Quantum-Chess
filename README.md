#   Quantum Checkers
### By Nicholas Karle
###       For Course CS 3650 Computer Architecture (Final Project)
####       Professor Nima Davarpanah
#       
####       Started: 12/13/2022
####       Functional: 12/14/2022      
####       Complete:
#   Controls
    Gates
    X - Place pauli-z-gate at cursor
    Y - Place pauli-y-gate at cursor
    Z - Place pauli-z-gate at cursor
    T - Place t-gate at cursor
    H - Place hadamard gate at cursor
    
    Control
    SPACE - Select at cursor
    C - place a control at cursor, controlling selected gate

    Notes
    Game does not recognize replacing a gate with itself
    You may however replace a controlled gate with an uncontrolled gate

#   Gameplay Outline
    Each player starts with 150 lives
    Each player can create a quantum circuit which is run 30 times at each measurement
    Each time their bit is resolved to a 1, they lose a life
    Only the second player may run and measure the circuit
    The game ends when one or both players goes below 1 life

# Credit
    Usage of some QPong assets from Qiskit