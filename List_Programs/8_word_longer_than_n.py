# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to find the list of words that are longer than n from a given list of words.

# method to find words longer than n
def longer_words(items, n):
    new_list = []
    for item in items:
        if len(item)>n:
            new_list.append(item)

    return new_list

# main method
def main():
    print(longer_words(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'],4))


if __name__ == "__main__":
    main()