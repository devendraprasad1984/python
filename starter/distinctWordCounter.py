# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

input_words="new to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"
words_arr=input_words.split(' ')
print("words string converted into array are",words_arr)
words_obj={}
for w in words_arr:
    words_obj[w]=words_obj.get(w,0)+1
print("distinct words and counter is",words_obj)