from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
import sys
filePath1 = sys.argv[1]
filePath2 = sys.argv[2]

def main():
    file1 = open(filePath1, encoding = 'utf-8', errors = "ignore")      #It opens the file with utf-8 encoding with errors ignored.
    file2 = open(filePath2, encoding = 'utf-8', errors = "ignore")      #Does the same thing as above

    word_set1 = tokenizer(file1)                                       #Words from file 1 are tokenized
    word_set2 = tokenizer(file2)                                       #Words from file 2 are tokenized

    repeat_set = add_to_set(word_set1, word_set2)                     #Set that has the words in common is created.
    output(repeat_set)

    file1.close()                                                   #Close the files
    file2.close()
        
#The runtime compleixity for this function is O(n). It has one for loop.
def tokenizer(file):
    entire_words = []
    final_set = set()
    for line in file:
        words = RegexpTokenizer("[a-zA-Z0-9]+").tokenize(line.lower()) #Every line is lowered and tokenized. They are divided into words and stored in the list using the regex pattern.
        entire_words = entire_words + words   #Entire words concatenate the word lists
    final_set = set(entire_words)   #Word lists are transformed into a set
    return final_set

#The runtime complexity for this function is O(min(len(s), len(t))). It uses set.intersection() method to find common words.
def add_to_set(word_set1, word_set2):
    repeat_set = set()      
    repeat_set = word_set1.intersection(word_set2)  #Find the words that are in both file 1 and file 2.
    return repeat_set

#The runtime complexity is O(1). It only prints the length of the given set.
def output(repeat_set):
    print(len(repeat_set))      #It prints out the length of the given set, which is the number of words that the files have in common.
    
if __name__ == "__main__":
    main()

#The entire program runs in the time complexity of O(m + n) because tokenizer function runs in O(n).
#Since there are two distinct files to open and read, complexity is O(m+n).
#It runs in the linear time relative to the size of the input. 
