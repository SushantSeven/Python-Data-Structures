# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to split a list based on first character of word.

# method to split a list based n first character
def split_list(ls):
    first_char_list = []
    for i in ls:
            if i[0] not in first_char_list:
                    print(i[0])
                    first_char_list.append(i[0])
                    for j in ls:
                        if j[0] == i[0]:
                            print(j)

# main method
def main():
    ls = ['About', 'Absolutely', 'After', 'Aint', 'Alabama','cat','Boy','cow', 'AlabamaBill', 'All', 'Also', 'Amos', 'And', 'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill', 'Billgone']
    print("The original list: ", ls)
    split_list(ls)


if __name__ == "__main__":
    main()