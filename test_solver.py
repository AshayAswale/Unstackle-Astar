import pytest
from single_file_solver import Solve
import numpy as np

def test_one():
    matrix = np.array([[1, 1]])
    capacity = 3
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_two():
    matrix = np.array([[1, 1]])
    capacity = 2
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_three():
    matrix = np.array([[1, 1]])
    capacity = 1
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_four():
    matrix = np.ones((2,2))
    capacity = 5
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_five():
    matrix = np.ones((2,2))
    capacity = 4
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_six():
    matrix = np.ones((2,2))
    capacity = 3
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_seven():
    matrix = np.ones((2,2))
    matrix[0,1] = 2
    capacity = 4
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_eight():
    matrix = np.ones((2,2))
    matrix[0,1] = 4
    matrix[0,0] = 2
    capacity = 4
    expected_output = 1
    assert Solve(matrix, capacity) == expected_output

def test_nine():
    matrix = np.ones((2,2))
    matrix[0,1] = 4
    matrix[1,1] = 3
    capacity = 4
    expected_output = 2
    assert Solve(matrix, capacity) == expected_output

def test_ten():
    matrix = np.matrix([[1,4,4],[2,2,1]])
    capacity = 4
    expected_output = 4
    assert Solve(matrix, capacity) == expected_output
    
def test_eleven():
    matrix = np.matrix([[2,4,4],[2,1,3]])
    capacity = 4
    expected_output = 4
    assert Solve(matrix, capacity) == expected_output

def test_twelve():
    matrix = np.matrix([[1,2,1],[2,2,1],[1,1,1],[1,2,2]])
    capacity = 6
    expected_output = 3
    assert Solve(matrix, capacity) == expected_output