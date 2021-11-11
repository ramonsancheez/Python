# Write a method that takes the array as an argument and returns this "outlier."
def find_outlier(integers):
    listaeven = 0
    listaeven1 = 0
    listaodd = 0
    listaodd1 = 0

    for i in integers:
        if i % 2 == 0:
            listaeven += i
            listaeven1 += 1
        else:
            listaodd += i
            listaodd1 += 1
    if listaodd1>1:
        return listaeven
    else:
        return listaodd           

if __name__ == "__main__":
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160
