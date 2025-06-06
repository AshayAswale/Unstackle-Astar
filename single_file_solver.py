import heapq
import math
import numpy as np
from collections import defaultdict
from copy import deepcopy


def Solve(grid:np.ndarray, CAPACITY:int):
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
  
  def getTopBoxInCol(column, curr_grid):
    x=0
    while x<ROWS and not curr_grid[x,column]:
      x+=1
    return -1 if x==ROWS else x
    
  def getHeuristicCost(updated_grid, remaining_capacity):
    total = np.sum(updated_grid)
    return math.ceil((total-remaining_capacity)/CAPACITY)
  
  def encodeDict(d:dict):
    s = ",".join("({},{})-{}".format(x,y,v) for (x,y),v in d.items())
    dict_lookup[s] = d
    return s

  def decodeDict(s:str):
    return dict_lookup[s]

  # cost estimate, current box, current weight, cluster_dict, updated_grid, 

  directions = ((0,1),(0,-1),(-1,0),(1,0))

  heap = []
  explored_state = set()

  heapq.heapify(heap)
  for y in range(COLS):
    x=getTopBoxInCol(y, grid)
    if x==-1:
      continue
    curr_node = (x, y)
    curr_grid = deepcopy(grid)
    curr_weight = curr_grid[curr_node]
    remaining_capacity = CAPACITY - curr_weight
    curr_grid[curr_node] = 0
    cost = getHeuristicCost(curr_grid, remaining_capacity)
    heapq.heappush(heap, (cost, curr_node, curr_weight, encodeDict({curr_node:1}), curr_grid))

  final_cost = float('inf')
  answer = {}
  max_len = 0

  while heap: 
    max_len = max(max_len, len(heap))
    curr_cost, (x,y), curr_weight, encoded_curr_allocation, curr_grid = heapq.heappop(heap)
    if encoded_curr_allocation in explored_state:
      continue
    curr_allocation = decodeDict(encoded_curr_allocation)
    if curr_cost>final_cost:
      continue
    
    nodes_to_add = set()
    reset = False
    for dx, dy in directions:
      nx,ny = x+dx, y+dy
      if isInvalid(nx,ny):
        continue
      if not isPickable(nx,ny,curr_grid):
        continue
      if grid[nx,ny]+curr_weight>CAPACITY:
        continue
      nodes_to_add.add(((nx,ny), reset))
    
    reset = True
    for ny in range(COLS):
      nx=getTopBoxInCol(ny, curr_grid)
      if nx==-1:
        continue
      nodes_to_add.add(((nx,ny), reset))
    
    for next_node, reset in nodes_to_add:
      curr_cluster = curr_allocation[(x,y)]
      next_grid = deepcopy(curr_grid)
      next_allocation = deepcopy(curr_allocation)

      next_weight = next_grid[next_node] if reset else next_grid[next_node]+curr_weight
      next_grid[next_node] = 0
      next_cost = max(curr_allocation.values())+getHeuristicCost(next_grid, CAPACITY-next_weight)
      if reset:
        next_cost += 1
      next_allocation[next_node] = curr_cluster+1 if reset else curr_cluster

      # if next_cost<=best_cost:
      if next_cost>final_cost:
        continue
      if np.all(next_grid==0):
        if next_cost<final_cost:
          final_cost = next_cost
          answer = next_allocation
        continue
      else:
        next_encoded_allocation = encodeDict(next_allocation)
        if next_encoded_allocation not in explored_state:
          heapq.heappush(heap, (next_cost, next_node, next_weight, next_encoded_allocation, next_grid))
    explored_state.add(encoded_curr_allocation)
  print("________________________________________________")
  print(answer)
  return max(answer.values()) if answer.values() else 0


if __name__ == '__main__':
    # grid = np.random.randint(1,5,(2,3))
    grid = np.matrix([[2,2,1,1],
                        [4,4,2,4],
                        [2,1,1,2],
                        [3,1,3,3]])
    # grid = np.random.randint(low=1, high=5, size=(2,2))
    print(grid)
    print(Solve(grid=grid, CAPACITY=6))