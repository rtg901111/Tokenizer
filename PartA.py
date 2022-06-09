#This file reads a file path, tokenizes the file into words, and prints out the sorted dictionary in the format of {word:frequency}.
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
import sys
filePath = sys.argv[1]

def main():
    file = open(filePath, encoding = 'utf-8', errors = "ignore")  #Open the file with utf-8 encoding with errors ignored
    final_dict = tokenizer(file)                                    #Calls tokenizer to create the frequency dictionary
    sorted_dict = sorter(final_dict)                                #Sorts the dictionary

    output(sorted_dict)                                             #Prints out the words and their frequency.

    file.close()                                                    #Close the file

#The runtime complexity for tokenizer function is O(n) because it has one simple for loop.
def tokenizer(file):
    entire_words = []
    final_dict = defaultdict(int)
    for line in file:
        words = RegexpTokenizer("[a-zA-Z0-9]+").tokenize(line.lower()) #Every line is lowered and tokenized. They are divided into words and stored in the list using the regex pattern.
        entire_words = entire_words + words   #Entire words concatenate the word lists
    for x in entire_words:
        final_dict[x] += 1      #Corresponding value in the dictionary is added by 1
    return final_dict

#The runtime complexity for this function is O(n log n). It sorts the dictionary.
def sorter(final_dict):
    sorted_dict = sorted(final_dict.items(), key = lambda x: (-x[1], x[0]))     #It sorts the dictionary as required; it is ordered by decreasing frequency and resolve ties alphabetically in ascending order.
    return sorted_dict

#The runtime complexity is O(n). It iterates over a dictionary to print out its keys and values.
def output(sorted_dict):
    for x in sorted_dict:
        print(x[0], "\t" ,x[1])     #It prints out the word and its frequency as the required format.

if __name__ == "__main__":
    main()

#PartA runs in O(n log n).
