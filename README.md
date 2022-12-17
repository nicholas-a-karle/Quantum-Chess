#   Quantum Checkers
### By Nicholas Karle
###       For Course CS 3650 Computer Architecture (Final Project)
####       Professor Nima Davarpanah

### Alternative Titles: Q-Chess
#       
####       Started: 12/13/2022
####       Functional: 12/14/2022      
####       Complete:

#
    Quantum Chess is a game played on two QBits with the X, Y, Z, T, and H gates, which can all be implemented with a single control. One GBit represents Player Zero and the other represents Player One. The reason for the name is that due to the nature of the game, each player has an equal number of actions they can perform up until a measurement. This causes the game to have to be played with sorts of traps I felt were similar to analagous moves in Chess.

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
    Only the second player may run and measure the circuit, but they lose that turn
    The game ends when one or both players goes below 1 life

#   How to start
    in console:
        python qchess.py

# Credit
    Usage of some QPong assets from Qiskit
    Usage of libaries