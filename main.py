#   Quantum Checkers
#       By Nicholas Karle
#
#       For Course CS 3650 Computer Architecture (Final Project)
#       Professor Nima Davarpanah
#       
#       Start:      12/13/2022
#       Complete:   
#       

#   Gameplay
#       goal is to force other player to be measured at 1 without you measuring at 1
#       rules:
#           take turns applying H, T, CX, X, Y, and Z gates to eachother
#               *CX may go either way
#           may call for measurement at any point, if they measure and 1 and you at 0, you score
#           otherwise, continue game as if nothing happened
#                   *to call for measurement, both players must have placed the same number of gates
#                   *caller is measured first
#           max number of gates is 9
