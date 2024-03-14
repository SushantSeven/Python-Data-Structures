# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title :  Write a Python program to generate all permutations of a list in Python.

from itertools import permutations # importing permutations from itertools

# method to display all the list permutations
def list_permu(items):
    new_list = list(permutations(items))
    for item in new_list:
        print(item)

# main method
def main():
    ls = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(f"The original list is: {ls}")
    list_permu(ls)


if __name__ == "__main__":
    main()