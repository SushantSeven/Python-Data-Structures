# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to clear a set.

# function to clear a set
def clear_set(set_var):
    return set_var.clear()
    
# main method
def main():
    set_var = {44,55,10,66,77,88}
    print("The original set: ",set_var)
    print("Cleared set: ",clear_set(set_var))


if __name__ == "__main__":
    main()