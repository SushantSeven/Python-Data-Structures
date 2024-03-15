# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to remove a key from a dictionary.

# function to remove a key from dictionary
def remove_item(dct, key):
    del dct[key]
    return dct
# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    key = 'Best'
    print("The original dictionary:",dct)
    print(f"After deleting key '{key}' from dictionary: {remove_item(dct, key)}")


if __name__=="__main__":
    main()