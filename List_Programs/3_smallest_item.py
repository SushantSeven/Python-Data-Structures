# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to get the smallest number from a list.

# function to find the smallest item in the list
def smallest(items):
    return min(items)

# main method 
def main():
    print(smallest([7,3,3,4,5,6,2]))

if __name__=="__main__":
    main()