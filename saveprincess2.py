#!/usr/bin/python
import random 

def dirty_cells(board):
  cells = []
  for idx,r in enumerate(board):
    for idy,c in enumerate(r): 
      if board[idx][idy] == "d":
        cells.append([idx, idy])
        return cells




def next_move(posr, posc, board):
  
    if board[posr][posc] == "d":
      return "CLEAN"
    
    cells = dirty_cells(board)
    
      
    if [posr, posc + 1] in cells:
      return "RIGHT"
    if [posr, posc - 1] in cells:
      return "LEFT"
    if [posr + 1, posc] in cells:
      return "DOWN"
    if [posr - 1, posc] in cells:
      return "UP"
    
    
    moves = ["RIGHT", "LEFT", "UP", "DOWN"]
    
    
    ok = False
    while ok == False:
      move = random.choice(moves)
      if move == "RIGHT" and ((posc + 1) < len(board)):
        ok = True
      if move == "LEFT" and ((posc - 1) >= 0):
        ok = True
      if move == "UP" and ((posr - 1) >= 0):
        ok = True
      if move == "DOWN" and ((posr + 1) < len(board)):
        ok = True
              
    return move

if __name__ == "__main__":
  pos = [int(i) for i in raw_input().strip().split()]
  board = [[j for j in raw_input().strip()] for i in range(5)]
  print next_move(pos[0], pos[1], board)
