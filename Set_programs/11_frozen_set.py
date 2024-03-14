# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to use of frozensets.

# function to use frozen set
def frozen_set(set_var):
    return frozenset(set_var)
    
# main method
def main():
    set_var = {44,55,10,66,77,88}
    print("The original set: ",set_var)
    print("The frozenset: ",frozen_set(set_var))
    

if __name__ == "__main__":
    main()