# Complete the function that takes 3 numbers x, y and k (where x ≤ y), and returns the number of integers within the range [x..y] (both ends included) that are divisible by k.
def divisible_number(x,y,k):
    count = 0

    for i in range(x, y + 1):
            if i % k == 0:
                count += 1
    return count

if __name__ == "__main__":
    assert divisible_number(6, 11, 2) == 3
    assert divisible_number(2, 20, 7) == 2
    assert divisible_number(1, 100, 2) == 50