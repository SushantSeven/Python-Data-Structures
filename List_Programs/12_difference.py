# @Author: Sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title :  Write a Python program to get the difference between the two lists.

# method to find the difference between two lists
def list_difference(ls1,ls2):
    new_list = []
    for i in ls1:
        if i not in ls2 and i not in new_list:
            new_list.append(i)
    for i in ls2:
        if i not in ls1 and i not in new_list:
            new_list.append(i)
    return new_list


# main method
def main():
    ls1 = [5,7,10,11]
    ls2 = [1,22,3,4,2,6,7,9,0]
    print(f"The original lists are: {ls1} {ls2}")
    print(f"The difference is: {list_difference(ls1,ls2)}")

if __name__ == "__main__":
    main()