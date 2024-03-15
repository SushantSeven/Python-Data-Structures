# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count number of items in a dictionary value that is a list.

# function to count number of items in a dictionary value that is a list.
def count_list_items(dct):
    count = 0
    for d in dct.items():
        if type(d[1]) is list:
            count+=1
    return count

# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': [1,2,3,4,5],'mm':[3,3,4]}
    print("The original dictionary:",dct)
    print("Number of keys that has values as list:",count_list_items(dct))


if __name__=="__main__":
    main()