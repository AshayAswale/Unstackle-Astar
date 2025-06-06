import pytest
from single_file_solver import Solve
import numpy as np

def test_one():
    # Grid: 
    # [1,1]
    matrix = np.array([[1, 1]])
    capacity = 3
    # Answer:
    # [P1,P1]
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_two():
    # Grid: 
    # [1,1]
    matrix = np.array([[1, 1]])
    capacity = 2
    # Answer:
    # [P1,P1]
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_three():
    # Grid: 
    # [1,1]
    matrix = np.array([[1, 1]])
    capacity = 1
    # Answer:
    # [P1,P2]
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_four():
    # Grid: 
    # [1,1]
    # [1,1]
    matrix = np.ones((2,2))
    capacity = 5
    # Answer:
    # [P1,P1]
    # [P1,P1]
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_five():
    # Grid: 
    # [1,1]
    # [1,1]
    matrix = np.ones((2,2))
    capacity = 4
    # Answer:
    # [P1,P1]
    # [P1,P1]
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_six():
    # Grid: 
    # [1,1]
    # [1,1]
    matrix = np.ones((2,2))
    capacity = 3
    # Answer:
    # [P1,P1]
    # [P1,P2]
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_seven():
    # Grid: 
    # [1,2]
    # [1,1]
    matrix = np.ones((2,2))
    matrix[0,1] = 2
    capacity = 4
    # Answer:
    # [P1,P1]
    # [P1,P2]
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_eight():
    # Grid: 
    # [2,4]
    # [1,1]
    matrix = np.ones((2,2))
    matrix[0,1] = 4
    matrix[0,0] = 2
    capacity = 4
    # Answer:
    # [P2,P1]
    # [P2,P2]
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_nine():
    # Grid: 
    # [1,4]
    # [1,3]
    matrix = np.ones((2,2))
    matrix[0,1] = 4
    matrix[1,1] = 3
    capacity = 4
    # Answer:
    # [P1,P2]
    # [P3,P3]
    expected_output = 3
    assert Solve(matrix, capacity) == expected_output

def test_ten():
    # Grid
    # [1,4,4]
    # [2,2,1]
    matrix = np.matrix([[1,4,4],[2,2,1]])
    capacity = 4
    # Answer
    # [P1,P2,P3]
    # [P1,P4,P4]
    expected_output = 4
    assert Solve(matrix, capacity) == expected_output
    
def test_eleven():
    # Grid
    # [2,4,4]
    # [2,1,3]
    matrix = np.matrix([[2,4,4],[2,1,3]])
    capacity = 4
    # Answer
    # [P1,P2,P3]
    # [P1,P4,P4]
    expected_output = 4
    assert Solve(matrix, capacity) == expected_output

def test_twelve():
    # Grid:
    # [1,2,1]
    # [2,2,1]
    # [1,1,1]
    # [1,2,2]
    matrix = np.matrix([[1,2,1],[2,2,1],[1,1,1],[1,2,2]])
    capacity = 6
    # Answer
    # [P1,P2,P2]
    # [P1,P2,P2]
    # [P1,P3,P3]
    # [P1,P3,P3]
    expected_output = 3
    assert Solve(matrix, capacity) == expected_output

def test_thirteen():
    # Grid
    # [2 2 1 1]
    # [4 4 2 4]
    # [2 1 1 2]
    # [3 1 3 3]
    matrix = np.matrix([[2,2,1,1],
                        [4,4,2,4],
                        [2,1,1,2],
                        [3,1,3,3]])
    capacity = 6
    # Answer
    # [P1 P1 P1 P1]
    # [P2 P3 P3 P5]
    # [P2 P4 P4 P5]
    # [P4 P4 P6 P6]
    expected_output = 6
    assert Solve(matrix, capacity) ==  expected_output

def test_fourteen():
    matrix = np.matrix([[4,2,3],
                        [2,2,2]])
    capacity = 6
    expected_output = 3
    assert Solve(matrix, capacity) == expected_output