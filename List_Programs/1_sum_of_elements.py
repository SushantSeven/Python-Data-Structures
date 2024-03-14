# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to sum all the items in a list.

# method to print all the elements of the list

def list_sum(elements):
    return sum(elements)

def main():
    ls = [1,2,4,22,10]
    print("The original list: ",ls)
    print(f"The sum of elements: {list_sum(ls)}")

if __name__ == "__main__":
    main()