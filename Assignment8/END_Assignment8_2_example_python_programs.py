# write a python function to check if a given string is a palindrome

def isPalindrome(s):
    return s == s[::-1]

# write a python function to check if a given string is symmetrical

def symmetry(a): 
      
    n = len(a) 
    flag = 0
      
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
          
    start1 = 0
    start2 = mid 
      
    while(start1 < mid and start2 < n): 
          
        if (a[start1]== a[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
       
    return flag

# write a function to reverse words of string

def rev_sentence(sentence):  
  
    words = sentence.split(' ')  
  
    reverse_sentence = ' '.join(reversed(words))  
  
    return reverse_sentence 

# write a program to check if a substring is present in a given string

string = "how are you?"
substring = "are"
if (string.find(substring) == -1): 
    print("NO") 
else: 
    print("YES")  

# write a program to print length of a string

str1 = "great way to learn!"
print(len(str1))

# write a program to print words frequncy in a given string

test_str = "It is a great meal at a great restaurant on a great day"
print("Original String: " + str(test_str))
res = {key: test_str.count(key) for key in test_str.split()} 
print("The words frequency: " + str(res))

# write a program to print even length words in a string

str1 = "I am doing fine"
s = str1.split(' ')
for word in s:  
    if len(word)%2==0: 
        print(word)  

# write a program to accept the strings which contains all vowels

str1 = "__main__"
if len(set(str1).intersection("AEIOUaeiou"))>=5: 
  print('accepted') 
else: 
  print("not accepted") 

# write a program to print count of number of unique matching characters in a pair of strings

str1="ababccd12@"
str2="bb123cca1@"

matched_chars = set(str1) & set(str2) 
print("No. of matching characters are : " + str(len(matched_chars)) )

# write a program to remove all duplicate characters from a string

str1 = "what a great day!"
print("".join(set(str1)))

# write a program to print least frequent character in a string

str1="watch the match"
all_freq = {} 
for i in str1: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print("Minimum of all characters is: " + str(res))

# write a program to print maximum frequency character in a string

str1 = "watch the match"
all_freq = {} 
for i in str1: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
res = max(all_freq, key = all_freq.get)
print("Maximum of all characters is: " + str(res))

# write a program to find and print all words which are less than a given length in a string

str1 = "It is wonderful and sunny day for a picnic in the park"
str_len = 5

res_str = [] 
      
text = str1.split(" ") 
      
for x in text: 

    if len(x) < str_len: 
        res_str.append(x) 

print("Words that are less than " + str(str_len) + ": " + str(res_str))

# write a program to split and join a string with a hyphen delimiter

str1 = "part of speech"
delimiter = "-"

list_str = str1.split(" ")

new_str = delimiter.join(list_str)

print("Delimited String is: " + new_str)

# write a program to check if a string is binary or not

str1="01110011 a"

set1 = set(str1)

if set1 == {'0','1'} or set1 == {'0'} or set1 == {'1'}:
    print("string is binary")
else:
    print("string is not binary")

# write a function to remove i-th indexed character in a given string

def remove_char(string, i):

    str1 = string[ : i]  

    str2 = string[i + 1: ] 
      
    return str1 + str2 

# write a function to find all urls in a given string

import re 
  
def find_urls(string): 
   
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)       
    return [x[0] for x in url] 

# write a function to find uncommon words from two strings

def UncommonWords(str1, str2): 
  
    count = {} 
      
    for word in str1.split(): 
        count[word] = count.get(word, 0) + 1
      
    for word in str2.split(): 
        count[word] = count.get(word, 0) + 1
  
    return [word for word in count if count[word] == 1]

# write a function to find common words from two strings

def commonWords(str1, str2): 
  
    count = {} 
      
    for word in str1.split(): 
        count[word] = count.get(word, 0) + 1
      
    for word in str2.split(): 
        count[word] = count.get(word, 0) + 1
  
    return [word for word in count if count[word] > 1]

# write a program to replace duplicate word occurence in String 

str1 = "IISC is the best. IISC has Classes in the evening for professionals. Classes help to learn new things."

repl_dict = {'IISC':'It', 'Classes': 'They'}

str_list = str1.split(' ') 

res = set() 

for idx, ele in enumerate(str_list): 
    if ele in repl_dict: 
        print(str(idx) + '  '+ele)
        if ele in res: 
            str_list[idx] = repl_dict[ele] 
        else: 
            res.add(ele)

res = ' '.join(str_list)

print("Replaced String: " + str(res))

# write a program to replace multiple words with a single word

str1 = 'CoffeeDay is best for coffee and having long conversations'
  
word_list = ["best", 'long'] 
  
repl_word = 'good'
  
res = ' '.join([repl_word if idx in word_list else idx for idx in str1.split()]) 

print("String after multiple replace : " + str(res))

# write a function to rotate string left by a given length  
  
def rotate_left(input,d):  
  
    Lfirst = input[0 : d]  
    Lsecond = input[d :]  
    return (Lsecond + Lfirst) 

# write a function to rotate string right by a given length  

def rotate_right(input,d):  
  
    Rfirst = input[0 : len(input)-d]  
    Rsecond = input[len(input)-d : ]  
    return (Rsecond + Rfirst) 

# write a function to replace all occurances of a substring in a string

str1 = "Hello! It is a Good thing"
substr1 = "Good"
substr2 = "bad"

replaced_str = str1.replace(substr1, substr2)

print("String after replace :" + str(replaced_str))

# write a program to move numbers to the end of a string

str1 = 'hi 123 how are you doing? 567 is with you. Take care of 89'
  
res = '' 
dig = '' 

for ele in str1: 
    if ele.isdigit(): 
        dig += ele 
    else: 
        res += ele 
  
res += dig 

print("Strings after digits at end : " + str(res))

# write a program to count characters surrounding vowels

str1 = 'week after week the numbers are increasing'
  
res = 0
vow_list = ['a', 'e', 'i', 'o', 'u']

for idx in range(1, len(str1) - 1): 

    if str1[idx] not in vow_list and (str1[idx - 1] in vow_list or str1[idx + 1] in vow_list): 
        res += 1
  
if str1[0] not in vow_list and str1[1] in vow_list: 
    res += 1
  
if str1[-1] not in vow_list and str1[-2] in vow_list: 
    res += 1

print("Characters around vowels count : " + str(res))

# write a function that return space count
 
def count_space(str1): 

    count = 0
      
    for i in range(0, len(str1)): 

        if str1[i] == " ": 
            count += 1
          
    return count

# write a program to break up string into individual elements

str1 = "whatisthis"
  
split_string = list(''.join(str1)) 
  
print(split_string) 

# write a program to extract string of N size and having K distict characters

str1 = 'GoodisalwaysGoood'
  
N = 3
  
K = 2
  
res = [] 

for idx in range(0, len(str1) - N + 1): 

    if (len(set(str1[idx: idx + N])) == K): 
        res.append(str1[idx: idx + N]) 
  
print("Extracted Strings : " + str(res)) 

# write a program to increment number which is at end of string

import re 
  
str1 = 'count001'

res = re.sub(r'[0-9]+$', 
             lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}",  
             str1) 
      
print("Incremented numeric String : " + str(res))

# write a program to calculate and print number of letters and digits in a string

str1 = "python1234"
  
total_digits = 0
total_letters = 0
  
for s in str1: 
  
    if s.isnumeric(): 
        total_digits += 1
    else: 
        total_letters += 1
  
print("Total letters found : ", total_letters) 
print("Total digits found : ", total_digits) 

# write a function to check if a lower case letter exists in a given string

def check_lower(str1):
    
    for char in str1: 
        k = char.islower()   
        if k == True: 
            return True 
    if(k != 1): 
        return False

# write a function to check if a upper case letter exists in a given string

def check_upper(str1):
    
    for char in str1: 
        k = char.isupper()   
        if k == True: 
            return True
    if(k != 1): 
        return False

# write a program to print number of words in a string

str1 = 'It is a glorious day'

res = len(str1.split()) 
  
print("The number of words in string are : " + str(res)) 

# write a program to print number of characters in a string

str1 = 'It is a glorious day'

res = len(str1) 

print("The number of characters in string are : ", str(res)) 


# -*- coding: utf-8 -*-
"""Assignment8 part2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AJziHejqYz4KvTmRtHGjOtnw69IZFGJA
"""

# write a funtion that accepts two lists of equal length and converts them into a dictioinary
def list_to_dict(list1, list2):
  return dict(zip(list1, list2))

# write a python function that accepts a list of dictionaries and sorts it by a specified key
def sort_dict_list(dict_list, sort_key):
  dict_list.sort(key=lambda item: item.get(sort_key))

# write a program to print the longest key in a dictioinary
dict_1 = {"key1": 10, "keeeey2": 2, "ky3": 30}
max_key=''
for key in dict_1:
  if len(key)>len(max_key):
    max_key=key
print(max_key)

# write a program to capitalize the first and last character of each key in a dictionary 
input_dict = {'key_a': 10, 'kEy': 2, 'Key_B': 13}
for key in list(input_dict.keys()):
  new_key = key[0].upper() + key[1:-1] + key[-1].upper()
  input_dict[new_key] = input_dict[key]
  if key != new_key:
    del input_dict[key]

# write a program that iterates over a dictionary and prints "Bingo!" if length of value is greater than the length of key. Otherwise print "no bingo"
key_val_map = {"key1": "length1", "key2": "len2", "Hello": "hi", "bingo": "print bingo"}
for key, val in key_val_map.items():
  if len(val) > len(key):
    print("Bingo!")
  else:
    print("no bingo")

# write a python function that accepts a dictionary that has unique values and returns its inversion
def invert_dict(input_dict):
  my_inverted_dict = {value: key for key, value in input_dict.items()}
  return my_inverted_dict

# write a function that inverts a dictionary with non-unique values. Keys that map to the same values should be appended to a list in the inverted dictionary
def invert_dict_non_unique(my_dict):
  my_inverted_dict = dict()
  for key, value in my_dict.items():
      my_inverted_dict.setdefault(value, list()).append(key)
  return my_inverted_dict

# write a program to merge a list of dictionaries into a single dictionary using dictionary comprehension
input = [{"foo": "bar", "Hello": "World"},
         {"key1": "val1", "key2": "val2"},
         {"sample_key": "sample_val"}]
merged_dict = {key: value for d in input for key, value in d.items()}

# write a function to return the mean difference in the length of keys and values of dictionary comprising of strings only.
def mean_key_val_diff(input_dict):
  sum_diff = 0
  for key, val in input_dict.items():
    sum_diff += abs(len(val) - len(key))
  return sum_diff/len(input_dict)

# write a program that prints the number of unique keys in a list of dictionaries.
list_of_dicts = [{"key1": "val1", "Country": "India"}, 
                 {"Country": "USA", "foo": "bar"},
                 {"foo": "bar", "foo2":"bar2"}]
unique_keys = []
for d in list_of_dicts:
  for key in d:
    if key not in unique_keys:
      unique_keys.append(key)
print(f"Number of unique keys: {len(unique_keys)}")

# write a Python program to replace the value of a particular key with nth index of value if the value of the key is list.
test_list = [{'tsai': [5, 3, 9, 1], 'is': 8, 'good': 10}, 
             {'tsai': 1, 'for': 10, 'geeks': 9}, 
             {'love': 4, 'tsai': [7, 3, 22, 1]}]   
N = 2
key = "tsai"  
for sub in test_list: 
    if isinstance(sub[key], list): 
        sub[key] = sub[key][N]

# write a program to convert a dictionary value list to dictionary list and prints it.
test_list = [{'END' : [5, 6, 5]}, {'is' : [10, 2, 3]}, {'best' : [4, 3, 1]}] 
res =[{} for idx in range(len(test_list))] 
idx = 0
for sub in test_list: 
	for key, val in sub.items(): 
		for ele in val: 
			res[idx][key] = ele 
			idx += 1
		idx = 0
print("Records after conversion : " + str(res))

# write a program to convert a list of dictionary to list of tuples and print it. 
ini_list = [{'a':[1, 2, 3], 'b':[4, 5, 6]}, 
            {'c':[7, 8, 9], 'd':[10, 11, 12]}] 
temp_dict = {} 
result = [] 
for ini_dict in ini_list: 
    for key in ini_dict.keys(): 
         if key in temp_dict: 
             temp_dict[key] += ini_dict[key] 
         else: 
             temp_dict[key] = ini_dict[key]   
for key in temp_dict.keys(): 
     result.append(tuple([key] + temp_dict[key])) 
print("Resultant list of tuples: {}".format(result))

# write a program that categorizes tuple values based on second element and prints a dictionary value list where each key is a category.
test_list = [(1, 3), (1, 4), (2, 3), (3, 2), (5, 3), (6, 4)] 
res = {} 
for i, j in test_list: 
     res.setdefault(j, []).append(i) 
print("The dictionary converted from tuple list : " + str(res))

# write a Python3 program that prints a index wise product of a Dictionary of Tuple Values     
test_dict = {'END Program' : (5, 6, 1), 'is' : (8, 3, 2), 'best' : (1, 4, 9)}
prod_list=[]
for x in zip(*test_dict.values()):
  res = 1 
  for ele in x: 
      res *= ele
  prod_list.append(res)
res = tuple(prod_list) 
print("The product from each index is : " + str(res))

# write a program to Pretty Print a dictionary with dictionary values. 
test_dict = {'tsai' : {'rate' : 5, 'remark' : 'good'}, 'cs' : {'rate' : 3}} 
print("The Pretty Print dictionary is : ") 
for sub in test_dict: 
    print(f"\n{sub}") 
    for sub_nest in test_dict[sub]: 
        print(sub_nest, ':', test_dict[sub][sub_nest])

# write a program to sort a nested dictionary by a key and print the sorted dictionary 
test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17}, 
             'Akshat' : {'roll' : 54, 'marks' : 12},  
             'Akash' : { 'roll' : 12, 'marks' : 15}} 
sort_key = 'marks'
res = sorted(test_dict.items(), key = lambda x: x[1][sort_key]) 
print("The sorted dictionary by marks is : " + str(res))

# write a python function to combine three lists of equal lengths into a nested dictionary and return it 
def lists_to_dict(test_list1, test_list2, test_list3):
  res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)] 
  return res

# write a program to print keys in a dictionary whose values are greater than a given input.
test_dict = {'tsai' : 4, 'random_key' : 2, 'foo' : 3, 'bar' : 'END'} 
K = 3
res = {key : val for key, val in test_dict.items() 
                   if type(val) != int or val > K} 
print("Values greater than K : ", res.keys())

# write a function that converts a integer dictionary into a list of tuples.
def dict_to_tuple(input_dict):
  out_tuple = [(a, b) for a,b in input_dict.items()]
  return out_tuple

# write a python function to return a flattened dictionary from a nested dictionary input
def flatten_dict(dd, separator ='_', prefix =''): 
    flattened =  { prefix + separator + k if prefix else k : v 
             for kk, vv in dd.items() 
             for k, v in flatten_dict(vv, separator, kk).items() 
             } if isinstance(dd, dict) else { prefix : dd } 
    return flattened

# write a program that prints dictionaries having key of the first dictionary and value of the second dictionary
test_dict1 = {"tsai" : 20, "is" : 36, "best" : 100} 
test_dict2 = {"tsai2" : 26, "is2" : 19, "best2" : 70} 
keys1 = list(test_dict1.keys()) 
vals2 = list(test_dict2.values()) 
res = dict() 
for idx in range(len(keys1)): 
	res[keys1[idx]] = vals2[idx] 
print("Mapped dictionary : " + str(res))

# write a program to combine two dictionaries using a priority dictionary and print the new combined dictionary.
test_dict1 = {'Gfg' : 1, 'is' : 2, 'best' : 3} 
test_dict2 = {'Gfg' : 4, 'is' : 10, 'for' : 7, 'geeks' : 12} 
prio_dict = {1 : test_dict2, 2: test_dict1} 
res = prio_dict[2].copy() 
for key, val in prio_dict[1].items(): 
    res[key] = val 
print("The dictionary after combination : " + str(res))

# write a Python program to combine two dictionary by adding values for common keys 
dict1 = {'a': 12, 'for': 25, 'c': 9} 
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300} 
for key in dict2: 
    if key in dict1: 
        dict2[key] = dict2[key] + dict1[key] 
    else: 
        pass

# write a Python program that sorts dictionary keys to a list using their values and prints this list.
test_dict = {'Geeks' : 2, 'for' : 1, 'CS' : 3} 
res = list(sum(sorted(test_dict.items(), key = lambda x:x[1]), ())) 
print("List after conversion from dictionary : ", res)

# write a program to concatenate values with same keys in a list of dictionaries. Print the combined dictionary.
test_list = [{'tsai' : [1, 5, 6, 7], 'good' : [9, 6, 2, 10], 'CS' : [4, 5, 6]}, 
             {'tsai' : [5, 6, 7, 8], 'CS' : [5, 7, 10]}, 
             {'tsai' : [7, 5], 'best' : [5, 7]}] 
res = dict() 
for inner_dict in test_list: 
    for inner_list in inner_dict: 
        if inner_list in res: 
            res[inner_list] += (inner_dict[inner_list]) 
        else: 
            res[inner_list] = inner_dict[inner_list]  
print("The concatenated dictionary : " + str(res))

# write a python program to print the top N largest keys in an integer dictionary.  
test_dict = {6 : 2, 8: 9, 3: 9, 10: 8}  
N = 4
res = []   
for key, val in sorted(test_dict.items(), key = lambda x: x[0], reverse = True)[:N]: 
    res.append(key) 
print("Top N keys are: " + str(res))

# write a program to print the values of a given extraction key from a list of dictionaries. 
test_list = [{"Gfg" : 3, "b" : 7},  
             {"is" : 5, 'a' : 10},  
             {"Best" : 9, 'c' : 11}]  
K = 'Best'
res = [sub[K] for sub in test_list if K in sub][0]   
print("The extracted value : " + str(res))

# write a program to convert date to timestamp and print the result
import time 
import datetime 
str1 = "20/01/2020"
element = datetime.datetime.strptime(str1,"%d/%m/%Y") 
timestamp = datetime.datetime.timestamp(element) 
print(timestamp)

# write a program to print the product of integers in a mixed list of string and numbers
test_list = [5, 8, "gfg", 8, (5, 7), 'is', 2] 
res = 1
for ele in test_list: 
    try: 
        res *= int(ele) 
    except : 
        pass
print("Product of integers in list : " + str(res))

