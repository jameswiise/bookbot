from stats import get_word_count
from stats import get_letter_count
from stats import print_report


from collections import Counter
from collections import OrderedDict
import sys



def main():
      
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    try:
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            content = file.read()

    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        sys.exit(1)

    text = content
    
    #print(text)
   
    split_words = text.split()
   
    get_word_count(split_words)
   
    lower_split = [letter for word in split_words for letter in word.lower()]
    
    get_letter_count(lower_split)

    dictionary = dict(Counter(lower_split)) 

    sorted_letters = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

    print_report(sorted_letters)
    





main()