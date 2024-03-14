# @Author: sushant Das

# @Date: 2024-03-14 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to slice a tuple.

# method to slice a tuple
def slice_tuple(items, index):
    new_tuple = tuple(items[i] for i in range(index))
    return new_tuple

        
# main method
def main():
    tup = (1,2,"Blue",True,3,"Red",4,5)
    index = 4
    print("The original tuple: ",tup)
    print(f"Tuple upto index {index}: {slice_tuple(tup,index)}")
        

if __name__=="__main__":
    main()