# Check if the columns and rows ara well done
def sudokuRow(sudoku): 
    for sublist in sudoku:
        for elements in sublist:
            oneNumber = sublist.count(elements)
            if oneNumber<2:
                pass
            else:
                return False
    return True

def sudokuColumn(sudoku): 
    lenSudoku = len(sudoku)
    for column in range(lenSudoku): 
        newList = [] 
        for sublist in sudoku: 
            number = sublist[column] 
            newList.append(number) 
        for i in newList:
            if newList.count(i) < 2:
                pass
            else:
                return False
    return True