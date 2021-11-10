#Narcissistic number is one that is equal to the sum of its digits raised to the power of its number of digits
def narcissistic(value):
    total = 0
    countNumber = len(str(value))
    for number in str(value):
        elevatedNumber = int(number)**countNumber
        total += elevatedNumber
    if total == value:
        return True
    else:
        return False


if __name__ == "__main__":
    assert narcissistic(153) == True 
    assert narcissistic(201) == False 
    assert narcissistic(259) == False
    assert narcissistic(371) == True
