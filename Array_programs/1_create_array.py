# @Author: Sushant Das

# @Date: 2024-03-15 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.

# importing array module
import array as arr
# funcion to create a an array
def create_array(item1,item2,item3,item4,item5):
    ary = arr.array('i',[item1,item2,item3,item4,item5])
    for i in ary:
        print(i, end=" ")
# main method
def main():
    item1 = 23
    item2 = 67
    item3 = 78
    item4 = 55
    item5 = 56
    create_array(item1,item2,item3,item4,item5)

if __name__ == "__main__":
    main()