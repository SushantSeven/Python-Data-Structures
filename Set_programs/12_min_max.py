# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to find maximum and the minimum value in a set.

# function to find min and max from a set
def min_max(set_var):
    return min(set_var), max(set_var)
    
# main method
def main():
    set_var = {44,55,10,66,77,88}
    print("The original set: ",set_var)
    print("the minimum value: ",min_max(set_var)[0])
    print("the maximum value: ",min_max(set_var)[1])
    

if __name__ == "__main__":
    main()