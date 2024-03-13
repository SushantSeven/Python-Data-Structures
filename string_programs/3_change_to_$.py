# 3. Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.

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