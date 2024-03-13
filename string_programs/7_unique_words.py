# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program that accepts a comma separated sequence of words as input
            # and prints the unique words in sorted form (alphanumerically).

# method to sort the list with unique characters
def unique_words(string_list):
    return (sorted(string_list))

# main method
def main():
    string_list = set(input("Enter the words as comma seperted values: ").split(","))
    print(unique_words(string_list))

if __name__=="__main__":
    main()