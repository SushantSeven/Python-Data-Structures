# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to check multiple keys exists in a dictionary.

# function to check if multiple keys exits in dictionary
def multi_keys(dct, keys):
    count = 0
    for k in keys:
        if k in dct:
            count += 1
    if len(keys)==count:
        return "Present"
    else:
        return "Not present"
# main method
def main():
    dct = {'Gfg': 5, 'is': 7, 'Best': 2, 'for': 9, 'geeks': 8}
    keys = ('Gfg','Best')
    print("The original dictionary:",dct)
    print("The keys:", keys)
    print(multi_keys(dct, keys))


if __name__=="__main__":
    main()