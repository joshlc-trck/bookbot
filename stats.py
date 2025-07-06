
def get_number_of_words(text):
    words = []
    num_words =0
    words = text.split()
    num_words = len(words)
    return num_words

def get_frequency_of_characters(text):
    histogram_of_characters = {}
    for i in text.lower():
        if i not in histogram_of_characters:
            histogram_of_characters[i] = 1
        else:       
            histogram_of_characters[i]+=1 
    return histogram_of_characters         

def sort_on(items):
    return items["num"]

def get_sorted_frequency_of_characters(dict_hist_char_num):
    list_of_char_freq = []
    for i in dict_hist_char_num:
        list_of_char_freq.append({"char": i,"num": dict_hist_char_num[i]})
    list_of_char_freq.sort(reverse=True ,key=sort_on)
    return list_of_char_freq
