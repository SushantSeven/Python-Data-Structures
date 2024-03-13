# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to multiplies all the items in a list.

# method to calculate the product of the items in a list
def item_product(items):
    sum = 1
    for item in items:
        sum *= item
    return sum

# main method
def main():
    print(item_product([1,2,3,4,5,6]))

if __name__=="__main__":
    main()
