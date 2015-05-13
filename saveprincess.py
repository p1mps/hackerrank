#!/bin/python

def whereIsCharacter(grid, character):
  for idx,x in enumerate(grid):
    for idy,y in enumerate(x):
      if(grid[idx][idy] == character):
        return idx,idy


def nextMove(n,r,c,grid):
  mario = whereIsCharacter(grid, "m")
  princess = whereIsCharacter(grid, "p")
  if mario[0] == princess[0]:
    if mario[1] > princess[1]:
      return "LEFT"
    else:
      return "RIGHT"
  if mario[1] == princess[1]:
    if mario[0] > princess[0]:
      return "UP"
    else:
      return "DOWN"
  if mario[0] > princess[0]:
    return "LEFT"
  else:
    return "RIGHT"
    
        
    


  print mario, princess
    
    
#print all the moves here
n = 5

grid = [['-','-','-','-','-'],
        ['-','-','-','-','-'],
        ['p','-','-','m','-'],
        ['-','-','-','-','-'],
]
r = 2
c = 5
# for i in xrange(0, m):
#   grid.append(raw_input().strip())

print nextMove(n,r,c,grid)
#displayPathtoPrincess(m,grid)
