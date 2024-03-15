# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.

# function to create a dictionary of string count
def string_count_dict(string):
    dct  = {}
    for s in string:
        v = string.count(s)
        dct.update({s:v})
    return dct

# main method
def main():
    string = 'w3resource'
    print("The original string:",string)
    print("The dictionary created:",string_count_dict(string))


if __name__=="__main__":
    main()