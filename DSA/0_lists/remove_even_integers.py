def remove_even(lst):
    return [item for item in lst if item % 2 != 0]

def remove_even2(lst):
    odds = []  # Create a new empty list
    for number in lst:  # Iterate over input list
        # Check if the item in the list is NOT even
        # ('%' is the modulus symbol!)
        if number % 2 != 0:
            odds.append(number)  # If it isn't even append it to the empty list
    return odds  # Return the new list

if __name__ == '__main__':
    list = [1, 2,3,4,5]
    print(remove_even(list))
