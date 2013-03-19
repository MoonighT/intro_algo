#This is a program calculate document distance between two documents
#Usage: document_distance.py filename1 filename2
import math
import sys
import string
def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except IOError:
        print "Error opening or reading the file: ",filename
        sys.exit()

translation_table = string.maketrans(string.punctuation+string.uppercase,
        " "*len(string.punctuation)+string.lowercase)

def get_words_from_line_list(text):
    """
    Parse the given text into words.
    Return list of all words found
    Using translate to get better performace
    """
    text = text.translate(translation_table)
    word_list = text.split()
    return word_list

def count_freq(word_list):
    D = {}
    for word in word_list:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D

def word_freq_for_file(filename):
    """
    Return sorted list of (word, freq)
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_map = count_freq(word_list)
    return freq_map


def inner_product(D1, D2):
    """
    Inner product between two vectors
    """
    sum = 0.0
    print D1, D2
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1, D2):
    """
    Input is two dicts for word
    Return the angle between these two vectors.
    """
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1)*inner_product(D2, D2))
    return math.acos(numerator/denominator)

def main():
    if len(sys.argv) != 3:
        print "Usage: document_distance filename1 filename2"
    else:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
        #get sorted word lists of two documents
        word_D1 = word_freq_for_file(filename1)
        word_D2 = word_freq_for_file(filename2)
        #calculate the distance using inner product of two lists
        distance = vector_angle(word_D1,word_D2)
        print "The distance between the documents is %0.6f (radians)"%distance

if __name__ == "__main__":
    main()

