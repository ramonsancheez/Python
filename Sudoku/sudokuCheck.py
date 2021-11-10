#Make a program that checks if the sudoku is well done

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,2]]

incorrect2 = [[1,2,3,4],
              [2,3,1,2],
              [4,1,2,3],
              [2,3,1,4]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]

irregular = [[1,2,3],
             [2,3,1]]

irregular2 = [[1,2,3],
             [2,3,1],
             [3,1]]
             
from sudokuCuadrado import matrizCuadrada
from sudokuInt import numInt
from sudokuColumnRow import sudokuRow, sudokuColumn
from sudokuRange import sudokuRange

def checkSudoku(sudoku):
    if matrizCuadrada(sudoku) and numInt(sudoku) and sudokuRange(sudoku) and sudokuRow(sudoku) and sudokuColumn(sudoku):
        return True
    else:
        return False

assert checkSudoku(correct) == True
assert checkSudoku(incorrect) == False
assert checkSudoku(incorrect2) == False
assert checkSudoku(incorrect4) == False
assert checkSudoku(incorrect3) == False
assert checkSudoku(incorrect5) == False
assert checkSudoku(irregular) == False
assert checkSudoku(irregular2) == False