# Global List
Stop_Words = [
    "i", "me", "my", "myself", "we", "our",
    "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he",
    "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs",
    "themselves", "what", "which", "who",
    "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be",
    "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing",
    "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with",
    "about", "against", "between", "into",
    "through", "during", "before", "after",
    "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then",
    "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not",
    "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will",
    "just", "don", "should", "now"
    ]

import re
import sys

def command_line_process():
    if (len(sys.argv) == 2):
        if sys.argv[1] == 'keep-digits':
            inp = input_text_lowercase()
            out1 = is_alnum(inp)
            out2 = stop_word_process(out1)
            out = ' '.join(out2)
            print(out.strip())
        elif sys.argv[1] == 'keep-stops':
            inp = input_text_lowercase()
            out1 = is_alnum(inp)
            out2 = remove_num(out1)
            out = ' '.join(out2)
            print(out.strip())
        elif sys.argv[1] == 'keep-symbols':
            inp = input_text_lowercase()
            out1 = remove_num(inp)
            out2 = stop_word_process(out1)
            out = ' '.join(out2)
            print(out.strip())
        else: 
            print('Optional command line argument does not match')
            exit('1') 
    elif len(sys.argv) > 2:
        exit('Too many arguments. Usage: python3 preprocess.py <mode>')
    else:
        inp = input_text_lowercase()
        out1 = is_alnum(inp)
        out2 = remove_num(out1)
        out3 = stop_word_process(out2)
        out = ' '.join(out3)
        print(out.strip())

def input_text_lowercase():
    inp_lst = list(map(str, input().split()))
    for i in range(len(inp_lst)):
        new_word = inp_lst[i].lower()
        inp_lst[i] = new_word
    return(inp_lst)    

def is_alnum(inp_lst):
    for word in inp_lst:
        new_word = re.sub(r'[\W_+]', '', word)
        inp_lst = list(map(lambda x: x.replace(word, new_word), inp_lst))
    return(inp_lst)

def remove_num(inp_lst):
    no_num_lst = []
    for word in inp_lst:
        if not(word.isnumeric()):
            new_word = "".join(x for x in word if not(x.isnumeric()))
        else:
            new_word = word
        no_num_lst.append(new_word)    
    return(no_num_lst)

def stop_word_process(inp_lst):
    processed_words = []
    for word in inp_lst:
        if word not in Stop_Words:
            processed_words.append(word)
    return(processed_words)


command_line_process()