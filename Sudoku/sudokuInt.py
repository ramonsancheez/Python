# Check if all the elements of sudoku are int
def numInt(sudoku):
    for sublist in sudoku:
        for element in sublist:
            if not isinstance(element, int):
                return False
    return True