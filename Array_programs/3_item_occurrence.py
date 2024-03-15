# @Author: Sushant Das

# @Date: 2024-03-15 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to get the number of occurrences of a specified element in an array.

# importing array module
import array as arr

# funcion to check if an element is present in array
def check_occurr(ary,item):
    count = 0
    for i in ary:
        if i == item:
            count += 1 
    return count
    
# main method
def main():
    ary = arr.array('i',[11,22,33,66,99,33])
    item = 33
    print("The original array is: ",ary)
    print(item,"occurred",check_occurr(ary,item), "times")

if __name__ == "__main__":
    main()