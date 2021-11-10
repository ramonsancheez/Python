# Check if the number of rows is the same number of the columns (square sudoku)   
def matrizCuadrada(sudoku):
    lengthY = len(sudoku)
    for element in sudoku:
        lengthX = len(element)
        if not lengthX == lengthY:
            return False
    return True
