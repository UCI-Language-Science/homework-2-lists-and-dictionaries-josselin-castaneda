# Write code that takes the provided list and removes all
# duplicates of numbers that have occurred earlier in the
# list, preserving the order otherwise
# 
# For the example below, the output should be
# "[1, 4, 3, 2, 5, 7, 9]"
# 
def duplicate_remover():
    duplicates_list = [1, 4, 3, 4, 2, 5, 1, 2, 7, 9, 4]
    non_duplicate = []

    for number in duplicates_list:
        if number not in non_duplicate:
            non_duplicate = non_duplicate + [number]
    print(non_duplicate)

if __name__ == "__main__":
    duplicate_remover()