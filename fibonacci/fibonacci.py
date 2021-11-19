#  Write a function that when given a number (n) returns the n-th number in the Fibonacci Sequence
def fibonacci(n):
    firstNumber = 0
    secondNumber = 1
    sum = 0
    count = 1
    
    while(count < n):    
        firstNumber = secondNumber
        secondNumber = sum
        sum= firstNumber + secondNumber
        count += 1	
    return sum

if __name__=="__main__":
    assert fibonacci(7) == 8
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
