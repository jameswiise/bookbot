from collections import Counter
from collections import OrderedDict

def get_word_count(split_words):
    count = 0
    for split_word in split_words:
        count += 1
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")




def get_letter_count(lower_split):
    dictionary = dict(Counter(lower_split))  
    #print(dictionary)
    sorted_letters = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    #print(sorted_letters)

def print_report(sorted_letters):
    for key, value in sorted_letters.items():
        if key.isalpha():
            
            print(f"{key}: {value}") 
    print("============= END ===============")


    