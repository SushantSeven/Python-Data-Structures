# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# function to print the string whose length is 2 or more and the starting and end element are same
def len_2_or_more(items):
    count = 0
    for item in items:
        if len(item) >= 2 and item[0] == item[len(item)-1]:
            count += 1
    return count

# main function
def main():
    print(len_2_or_more(['abc', 'xyz', 'aba', '1221','aa','cdnc']))

if __name__=="__main__":
    main()