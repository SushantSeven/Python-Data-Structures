# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to add member(s) in a set.

# function to add member to a set
def add_item(set_var, element):
    set_var.add(element)
    return set_var
    

# main method
def main():
    set_var = {11,22,33,44,55}
    element = 77
    print("The original set: ",set_var)
    print("Updated set: ",add_item(set_var, element))

if __name__ == "__main__":
    main()