# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to get a string from a given string where all occurrences of its
#          first char have been changed to '$', except the first char itself.

# method to replace 
def replace_char(string):    
    new_string = string.lower()
    ls =[]
    for i in range(len(new_string)):
        if new_string[i]== new_string[0] and i != 0:
            ls.append("$")
        else:
            ls.append(new_string[i])
    print("".join(ls))

def main():
    string = input("Enter a string: ")
    replace_char(string)


if __name__ == "__main__":
    main()