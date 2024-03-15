# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python script to sort (ascending and descending) a dictionary by value.

# function sort the dictionary in ascending order
def sort_dict_asc(dct):
    new_dct = {}
    for key, value in sorted(dct.items(), key = lambda x: x[1]):
        new_dct.update({key:value})
    return new_dct
# function sort the dictionary in descending order
def sort_dict_desc(dct):
    new_dct = {}
    for key, value in sorted(dct.items(), key = lambda x: x[1], reverse=True):
        new_dct.update({key:value})
    return new_dct

# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    print("The original dictionary:",dct)
    print("Dictionary after sorting by value in ascending order",sort_dict_asc(dct))
    print("Dictionary after sorting by value in descending order",sort_dict_desc(dct))


if __name__=="__main__":
    main()