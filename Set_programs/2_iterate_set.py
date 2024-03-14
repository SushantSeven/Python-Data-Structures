# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to iteration over sets.

# function to iterate a set
def iterate_set(set_var):
    for i in set_var:
        print(i)
    

# main method
def main():
    set_var = {11,22,33,44,55}
    print("The original set: ",set_var)
    iterate_set(set_var)

if __name__ == "__main__":
    main()