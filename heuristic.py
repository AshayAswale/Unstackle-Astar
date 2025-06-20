import heapq
import math
import numpy as np
from collections import defaultdict
from copy import deepcopy


def HeuristicSolve(grid:np.ndarray, CAPACITY:int):
  ROWS, COLS = grid.shape
  TOTAL = ROWS*COLS
  dict_lookup={}

  def isInvalid(x,y):
    return x<0 or y<0 or x>=ROWS or y>=COLS

  def isPickable(x,y,curr_grid):
    if x==0: 
      return True
    if curr_grid[x,y]==0:
      return False
    if x>0:
      return curr_grid[x-1,y]==0
  
  # cost estimate, current box, current weight, cluster_dict, updated_grid, 

  directions = ((0,-1),(0,1),(1,0),(-1,0))

  answer = {}
  curr_group = 0
  root = (0,0)
  while len(answer)<ROWS*COLS: 
    curr_group += 1
    while root in answer:
      x,y = root
      root = (x,y+1)
      if isInvalid(root[0], root[1]):
        root = (x+1,0)
    curr_weight = grid[root]
    grid[root] = 0
    answer[root] = curr_group
    
    def recursiveAddition(node):
      nonlocal curr_weight
      x,y = node
      for dx, dy in directions:
        nx,ny = x+dx, y+dy
        if isInvalid(nx,ny):
          continue
        if not isPickable(nx,ny,grid):
          continue
        if not grid[nx,ny]:
          continue
        if grid[nx,ny]+curr_weight>CAPACITY:
          continue
        answer[(nx,ny)] = curr_group
        curr_weight+=grid[nx,ny]
        grid[nx,ny] = 0
        recursiveAddition((nx,ny))
    recursiveAddition(root)
  print("________________________________________________")
  print(answer)
  return curr_group


if __name__ == '__main__':
    grid = np.random.randint(1,5,(15,15))
    # grid = np.matrix([[2,2,1,1],
    #                     [4,4,2,4],
    #                     [2,1,1,2],
    #                     [3,1,3,3]])
    # grid = np.matrix([[1,2],
    #                   [1,2]])
    # grid = np.random.randint(low=1, high=5, size=(2,2))
    print(grid)
    print(Solve(grid=grid, CAPACITY=6))