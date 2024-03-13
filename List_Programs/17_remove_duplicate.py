# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove duplicates from a list of lists.

# method to find common items in a list
def remove_duplicate(items):
    new_list = list()
    for item in items:
        if item not in new_list:
            new_list.append(item)

    return new_list

# main method
def main():
    print(remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40],[33],[40]]))


if __name__ == "__main__":
    main()