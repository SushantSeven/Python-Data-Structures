# @Author: Sushant Das

# @Date: 2024-03-15

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python script to concatenate following dictionaries to create a new one.

# function to concatenate dictionaries
def concat_dict(dic1,dic2,dic3):
    new_dic = {}
    for d in [dic1,dic2,dic3]:
        new_dic.update(d)
    return new_dic
# main method
def main():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}
    print("The original dictionary:",dic1,dic2,dic3)
    print("Dictionary after conatenation ",concat_dict(dic1,dic2,dic3))


if __name__=="__main__":
    main()