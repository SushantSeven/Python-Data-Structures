# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# method to desiplay upper case and lower case
def upper_lower(string):
    return string.upper(), string.lower()

# main method
def main():
    string = input("Enter a string: ")
    print(*(upper_lower(string)))

if __name__ == "__main__":
    main()