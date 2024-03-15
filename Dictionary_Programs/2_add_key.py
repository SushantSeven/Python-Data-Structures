# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python script to add a key to a dictionary.

# function to add a new key value to dictionary
def add_dict(dct,new):
    dct.update(new)
    return dct
# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    new = {'abc': 4}
    print("The original dictionary:",dct)
    print("Dictionary after adding new key value",add_dict(dct,new))


if __name__=="__main__":
    main()