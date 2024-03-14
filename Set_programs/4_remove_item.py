# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove item(s) from set

# function to remove items from a set
def remove_item(set_var, item1,item2):
    ls = [item1,item2]
    for i in ls:
        set_var.remove(i)
    return set_var
    

# main method
def main():
    set_var = {11,22,33,44,55}
    item1 = 22
    item2 = 33
    print("The original set: ",set_var)
    print("Updated set: ",remove_item(set_var,item1,item2))

if __name__ == "__main__":
    main()