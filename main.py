#print("greetings boots")
import sys
from stats import get_number_of_words
from stats import get_frequency_of_characters
from stats import get_sorted_frequency_of_characters

def get_book_text(path_to_file): 
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def display_as_req(list,number):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for l in list:
        if l['char'].isalpha():
            print(f"{l['char']}: {l['num']}")
    return



def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    
    the_book = get_book_text(sys.argv[1])
    
    #Takes text and gives the number of words 
    number = get_number_of_words(the_book)
    #print(f"{number} words found in the document")
    
    
    #Takes a book and returns frequency of characters as a dictionary char : number pair
    dict = get_frequency_of_characters(the_book)
    
    #Takes a dictionary of character number pair, sorts it and returns a list of dictionaries {'char' : character ,'num' : freq_of_char }
    list_of_char_freq = get_sorted_frequency_of_characters(dict)
    
    #Calling a function to display based on specifications
    display_as_req(list_of_char_freq,number)
    
    
    #print(list_of_char_freq)
    #print(dict)    
    #print(the_book)  

main()