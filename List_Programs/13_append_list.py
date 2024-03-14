# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title :  Write a Python program to append a list to the second list.

# method to append one list to another
def append_list(list1, list2):
    return(list1+list2)

# main method
def main():
    ls1 = [5,7,10,11]
    ls2 = [1,22,3,4,2,6,7,9,0]
    print(f"The original lists are: {ls1} {ls2}")
    print(f"The appended list is: {append_list(ls1,ls2)}")


if __name__ == "__main__":
    main()