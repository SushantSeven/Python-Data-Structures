# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to add 'ing' at the end of a given string (length should be at
#           least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

#           given string is less than 3, leave it unchanged.

# method to add ing or ly at the end of a string
def add_ing_ly(string):
    if len(string) >= 3:
        if string.endswith("ing"):
            return string+"ly"
        else:
            return string+"ing"
    else:
        return string

# main method
def main():
    string = input("Enter the string: ")
    print(add_ing_ly(string))

if __name__ == "__main__":
    main()