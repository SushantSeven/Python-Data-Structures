# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to iterate over dictionaries using for loops.

# function to iterate dictionary
def iter_dict(dct):
    for key,value in dct.items():
        print(key, value)
# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    print("The original dictionary:",dct)
    iter_dict(dct)


if __name__=="__main__":
    main()