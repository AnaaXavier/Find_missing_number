last_number = 16 # One more than the actual desired number, since the range is up to last_number - 1

numbers_list = [numbers for numbers in range(1, last_number) if numbers != 2] # creates a list with a missing number, in this case, it's number 2

# holds the expected collection of numbers without any missing number
expected_numbers_set = set(range(1, last_number))
# the current number list converted to sets
numbers_set = set(numbers_list) 

difference_of_sets = list(expected_numbers_set - numbers_set)[0]

print(f"\nThe set with missing number: {numbers_set}\nThe expected set of numbers: {expected_numbers_set}")
print(f"\nThe missing number is: {difference_of_sets}")