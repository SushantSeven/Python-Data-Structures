# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title :  Write a Python program to find common items from two lists.

# method to find common items in a list
def append_list(list1, list2):
    new_list = list()
    for i in list1:
        if (i in list2) and (i not in new_list):
            new_list.append(i)
    return new_list

# main method
def main():
    ls1 = [1,22,3,4,2,6,7,9,0]
    ls2 = [1,7,9,7,10,11]
    print(f"The original lists are: {ls1} {ls2}")
    print(f"The common items are: {append_list(ls1,ls2)}")


if __name__ == "__main__":
    main()