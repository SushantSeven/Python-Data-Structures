# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove an item from a set if it is present in the set.

# function to remove item from a set if it is present
def remove_item(set_var, item):
    if item in set_var:
        set_var.remove(item)
        return set_var
    else:
        return set_var
    

# main method
def main():
    set_var = {11,22,33,44,55}
    item = 22
    print("The original set: ",set_var)
    print("Updated set: ",remove_item(set_var,item))

if __name__ == "__main__":
    main()