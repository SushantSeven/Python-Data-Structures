# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# function to print the string whose length is 2 or more and the starting and end element are same
def len_2_or_more(items):
    new_items = list()
    count = 0
    for item in items:
        if len(item) >= 2 and item[0] == item[len(item)-1]:
            new_items.append(item)
            count += 1
    return new_items, count

# main function
def main():
    ls = ['abc', 'xyz', 'aba', '1221','aa','cdnc']
    result = len_2_or_more(['abc', 'xyz', 'aba', '1221','aa','cdnc'])
    print(f"The original list is: {ls}")
    print(f"The number of elements greater length than 2 are {result[1]}")
    print("The elements greater length than 2 are: ",*result[0])

if __name__=="__main__":
    main()