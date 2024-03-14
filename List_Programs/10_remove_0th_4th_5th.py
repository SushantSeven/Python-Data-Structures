# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# method to remove 0th 4th 5th index items
def remove_items(items):
    items.pop(5)
    items.pop(4)
    items.pop(0)
    return items

# main method
def main():
    ls = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(f"The original list is: {ls}")
    print(f"The updated list is: {remove_items(ls)}")

if __name__ == "__main__":
    main()