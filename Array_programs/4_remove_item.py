# @Author: Sushant Das

# @Date: 2024-03-15 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove the first occurrence of a specified element from an array.

# importing array module
import array as arr
# funcion to remove item from an array
def remove_item(ary,item):
    for i in ary:
        if i == item:
            ary.remove(i)
            return ary
    return ary
# main method
def main():
    ary = arr.array('i',[11,22,33,66,99,33])
    item = 33
    print("The original array: ",ary)
    print("The updated array after removing first occurrence of",item, remove_item(ary,item))

if __name__ == "__main__":
    main()