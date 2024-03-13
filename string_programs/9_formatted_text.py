# @Author: Sushant Das

# @Date: 2024-03-13 

# @Last Modified by: Author Name

# @Last Modified time: 2021-02-11 18:00:30

# @Title : Write a Python program to display formatted text (width=50) as output.

# importing textwrap module
import textwrap

def format_string(string):
    print(textwrap.fill(string,width=50))

def main():
    string = '''Fairfax Harrison (March 13, 1869 – February 2, 1938) was an American lawyer and
    businessman. He became a lawyer for the Southern Railway Company in 1896, and by 1906 
    he was the company's vice-president of finance. In 1913 he was elected president of Southern; 
    under his leadership, the company expanded to an 8,000-mile (13,000 km) network across 13 states.
    Following the United States's entry into World War I, the federal government took control of the railroads, 
    running them through the United States Railroad Administration, on which Harrison served. 
    After the war, Harrison worked to improve the railroad's public relations, upgrade the locomotive stock by introducing
    more powerful engines, increase the company's amount of railroad track and extend the area serviced by the railway. Harrison struggled 
    to keep the railroad afloat during the Great Depression, but by 1936 Southern was once again profitable. Harrison retired in 1937 and 
    died three months later.'''
    format_string(string)

main()