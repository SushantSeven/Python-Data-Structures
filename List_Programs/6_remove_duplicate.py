# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove duplicates from a list.

# method to remove duplicate items from the list
def remove_dupli(items):
    new_items = []
    for item in items:
        if item not in new_items:
            new_items.append(item)
    return new_items

# main method
def main():
    print(remove_dupli([1,22,3,4,1,2,6,6,7,9,0,0]))

if __name__ == "__main__":
    main()