#  Create a function that takes an amount of US currency in cents, and returns a dictionary/hash which shows the least amount of coins used to make up that amount
def loose_change(cents):
    KeysValues = {"Nickels": 5, "Pennies": 1, "Dimes": 10, "Quarters": 25} 
    ordenatedValues = sorted(KeysValues.values(), reverse = True) 

    change = []
    i = 0
    while cents > 0:
        if cents < 1:
            break
        elif cents >= ordenatedValues[i]:
            cents -= ordenatedValues[i]
            change.append(ordenatedValues[i])
        else:
            i += 1

    change_dict = dict.fromkeys(["Nickels", "Pennies", "Dimes", "Quarters"], 0)
    for value in KeysValues: 
        for changeValue in change: 
            if KeysValues[value] == changeValue:
                change_dict[value] += 1
    return change_dict
     
if __name__ == "__main__":
     assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1} 
     assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0} 
     assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0} 