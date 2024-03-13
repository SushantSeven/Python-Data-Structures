# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def sort_list(items):
    items.sort(key = lambda item: item[1])
    return items

# main method
def main():
    print(sort_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

if __name__ == "__main__":
    main()