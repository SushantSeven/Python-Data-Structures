# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to clone or copy a list.

# method to clone a copy of a list
def clone_a_list(items):
    clone = items
    return clone

# main method
def main():
    ls = [1,22,3,4,1,2,6,6,7,9,0,0]
    print(f"The original list is: {ls}")
    print(f"The cloned list is: {clone_a_list(ls)}")

if __name__ == "__main__":
    main()