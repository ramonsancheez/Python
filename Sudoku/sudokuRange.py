# Check that no sudoku element is bigger than the range 
def sudokuRange(sudoku):
    lenSudoku = len(sudoku)
    for sublist in sudoku:
        for element in sublist:
            try:
                if element > lenSudoku or element < 0:
                    return False
            except:
                return False
    return True