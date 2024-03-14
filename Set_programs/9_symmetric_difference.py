# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create a symmetric difference.

# function to create symmetric difference
def sym_difference(set_var1, set_var2):
    return set_var1.symmetric_difference(set_var2)
    
# main method
def main():
    set_var1 = {11,22,33,44,55}
    set_var2 = {44,55,10,66,77,88}
    print("The original set: ",set_var1,set_var2)
    print("The difference of sets: ",sym_difference(set_var1,set_var2))


if __name__ == "__main__":
    main()