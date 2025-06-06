import heapq
import numpy as np
from collections import defaultdict
from copy import deepcopy


def Solve(grid, CAPACITY):
  ROWS, COLS = len(grid), len(grid[0])
  TOTAL = ROWS*COLS

  def isInvalid(x,y):
    return x<0 or y<0 or x>=ROWS or y>=COLS

  closed_set = set()

  # remaining boxes, current box, current weight, current cluster, currently allocated (local)

  directions = ((0,1),(0,-1),(-1,0))

  heap = []
  heapq.heapify(heap)
  curr_node = (ROWS-1, 0)
  heapq.heappush(heap, (TOTAL-1, curr_node, grid[curr_node], {curr_node:1}, curr_node))

  final_cost = float('inf')
  best_allocation = set()
  answer = {}

  while heap:
    current_cost, (x,y), current_weight, current_allocation, root = heapq.heappop(heap)
    
    if current_cost > final_cost:
      continue
    
    for dx, dy in directions:
      nx,ny = x+dx, y+dy
      if isInvalid(nx,ny):
        continue
      if (nx,ny) in closed_set:
        continue
      if (nx,ny) in current_allocation:
        continue

      current_cluster = current_allocation[(x,y)]
      if grid[nx,ny]+current_weight<=CAPACITY:
        next_weight = grid[nx,ny]+current_weight
        next_cluster = current_cluster
        next_cost = current_cost-1
        next_root = root
      else:
        nx,ny=root
        while (nx,ny) in current_allocation:
          ny+=1
          if isInvalid(nx,ny):
            nx-=1
            ny=0
            if nx<0:
              break
            
        next_weight = grid[nx,ny]
        next_cluster = current_cluster+1
        next_cost = TOTAL - len(current_allocation)
        next_root = (nx,ny)
          

      next_allocation = (current_allocation)
      next_allocation[(nx,ny)] = next_cluster

      # if next_cost<=best_cost:
      heapq.heappush(heap, (next_cost, (nx,ny), next_weight, next_allocation, next_root))
      if len(next_allocation)==TOTAL and next_cost<final_cost:
        answer = deepcopy(next_allocation)
        final_cost = next_cost
      
    closed_set.add((x,y))
  print("________________________________________________")
  print(answer)
  return max(answer.values()) if answer.values() else 0