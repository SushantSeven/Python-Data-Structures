# function to return the longest string in the list
def longest(string_list):
    index_list = []
    for i in string_list:
        index_list.append(len(i))
    return string_list[index_list.index(max(index_list))]

# main method
def main():
    string_list = input("Enter the words as comma seperated values: ").split(" ")
    print(longest(string_list))

if __name__ == "__main__":
    main()