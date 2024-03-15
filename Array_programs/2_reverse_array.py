# @Author: Sushant Das

# @Date: 2024-03-15 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to reverse the order of the items in the array.

# importing array module
import array as arr
# funcion to reverse an array
def reverse_array(ary):
    ary.reverse()
    return ary
# main method
def main():
    ary = arr.array('i',[11,22,33,44,55])
    print("The original array: ",ary)
    print("The reversed array: ",reverse_array(ary))

if __name__ == "__main__":
    main()