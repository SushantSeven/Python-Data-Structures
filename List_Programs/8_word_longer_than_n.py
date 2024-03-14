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
    ls = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    n = 4
    print(f"The original list is: {ls}")
    print(f"The value of n is {n}")
    print(f"Words longer tha {n} are: {longer_words(ls,n)}")


if __name__ == "__main__":
    main()