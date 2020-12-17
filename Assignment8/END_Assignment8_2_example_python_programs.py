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