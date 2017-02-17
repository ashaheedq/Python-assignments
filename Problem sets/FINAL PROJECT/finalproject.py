# Abdulshaheed Alqunber
# asq@bu.edu
# Final Project part I & II
from math import *

def clean_text(txt):
    """takes a string of text txt as a parameter and returns a list
    containing the words in txt after it has been cleaned"""

    # lowering the letters
    txt = txt.lower()

    #code to clean text from punctuation
    txt = txt.replace('.', '')
    txt = txt.replace(',', '')
    txt = txt.replace('?', '')
    txt = txt.replace('!', '')
    txt = txt.replace('"', '')
    txt = txt.replace('.', '')
    txt = txt.replace(':', '')
    txt = txt.replace(';', '')
    txt = txt.replace('-', '')
    txt = txt.replace('[', '')
    txt = txt.replace(']', '')
    txt = txt.replace('(', '')
    txt = txt.replace(')', '')
    return txt

def stem(word):
    """ accepts a string as a parameter and return the stem of s.
    The stem of a word is the root part of the word,
    which excludes any prefixes and suffixes
    """

    word = word.lower()

    if word[-3:] == 'ier':
        word = word[:-3] + 'y'
        return stem(word)

    elif word[-4:] == 'iers':
        word = word[:-4] + 'y'
        return stem(word)

    elif word[-2:] == 'er' and len(word) > 5:
        word = word[:-2]
        return stem(word)

    elif word[:3] == 'pre':
        word = word[3:]
        return stem(word)

    elif word[:2] == 'un':
        word = word[2:]
        return stem(word)

    elif word[:2] == 'in':
        word = word[2:]
        return stem(word)

    elif word[-3:] == 'ing' and len(word) > 5:
        word = word[:-3]
        return stem(word)

    elif word[-2:] == 'ed' and len(word) > 4:
        word = word[:-2]
        return stem(word)

    elif word[-3:] == 'ies':
        word= word[:-2]
        return stem(word)

    elif word[-4:] == 'ment' and len(word) > 7:
        word = word[:-4]
        return stem(word)

    elif word[-4:] == 'able' and len(word) > 6:
        word = word[:-4]
        return stem(word)

    elif word[-3:] == 'ful':
        word = word[:-3]
        return stem(word)

    elif word[-2:] == 'ly' and len(word) > 4:
        word = word[:-2]
        return stem(word)

    elif word[:2] == 're' and len(word) > 4:
        word = word[2:]
        return stem(word)

    elif word[-4:] == 'ness' and len(word) > 4:
        word = word[:-4]
        return stem(word)

    elif word[-5:] == 'ality':
        word = word[:-3]
        return stem(word)

    elif word[:3] == 'dis':
        word = word[3:]
        return stem(word)

    elif word[:3] == 'non':
        word = word[3:]
        return stem(word)

    elif word[:3] == 'sub':
        word = word[3:]
        return stem(word)

    elif word[:3] == 'mis':
        word = word[3:]
        return stem(word)

    return word



class TextModel:

    def __init__(self, model_name):
        """constructs a new TextModel object by accepting a string model_name
        as a parameter and initializing the following three attributes:
        • name – a string that is a label for this text model, such as 'JKRowling' or 'Shakespeare'.
        • words – a dictionary that records the number of times each word appears in the text.
        • word_lengths – a dictionary that records the number of times each word length appears.
        """

        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        words = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        self.number_of_punctuation = 0

    def __repr__(self):
        """returns a string that includes the name of the
        model as well as the sizes of the dictionaries"""

        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of punctuation: ' + str(self.number_of_punctuation)
        return s

    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
        to all of the dictionaries in this text model """

        # update sentence_lengths dictionary
        text = s.split(' ')
        counter = 0
        for i in text:
            counter += 1
            if '.' in i or '?' in i or '!' in i:
                if counter in self.sentence_lengths:
                    self.sentence_lengths[counter] += 1
                    counter = 0
                else:
                    self.sentence_lengths[counter] = 1
                    counter = 0

        # update punctuation dictionary
        text = s.split(' ')
        punctuation_list = ':;?!.",'
        for i in text:
            for r in punctuation_list:
                if r in i:
                    self.number_of_punctuation += 1
                    if r in self.punctuation:
                        self.punctuation[r] += 1
                    else:
                        self.punctuation[r] = 1


        # code to clean the text and split it into a list of words.
        word_list = clean_text(s)
        word_list = word_list.split(' ')

        # update words dictionary
        for w in word_list:
            if w in self.words:
                self.words[w] += 1
            else:
                self.words[w] = 1

        # update word_lengths dictionary
        for w in word_list:
            if len(w) in self.word_lengths:
                self.word_lengths[len(w)] += 1
            else:
                self.word_lengths[len(w)] = 1

        # update stems dictionary
        for w in word_list:
            if stem(w) in self.stems:
                self.stems[stem(w)] += 1
            else:
                self.stems[stem(w)] = 1

    def add_file(self, filename):
        """adds all of the text in the file identified by filename to the model"""

        f = open(filename, 'r', encoding='utf8', errors='ignore')
        read_text = f.read()
        self.add_string(str(read_text))

    def save_model(self):
        """saves the TextModel object self by writing
        its various feature dictionaries to files"""

        # words
        filename = self.name + '_' + 'words'
        f = open(filename, 'w' )     # Open file for writing.
        f.write(str(self.words))     # Writes the dictionary to the file.
        f.close()                    # Close the file.

        #word_lengths
        filename1 = self.name + '_' + 'word_lengths'
        f = open(filename1, 'w' )     # Open file for writing.
        f.write(str(self.word_lengths))     # Writes the dictionary to the file.
        f.close()                    # Close the file.

        #stems
        filename2 = self.name + '_' + 'stems'
        f = open(filename2, 'w' )     # Open file for writing.
        f.write(str(self.stems))     # Writes the dictionary to the file.
        f.close()                    # Close the file.

        #word_lengths
        filename3 = self.name + '_' + 'sentence_lengths'
        f = open(filename3, 'w' )     # Open file for writing.
        f.write(str(self.sentence_lengths))     # Writes the dictionary to the file.
        f.close()                    # Close the file.

        #word_lengths
        filename4 = self.name + '_' + 'punctuation'
        f = open(filename4, 'w' )     # Open file for writing.
        f.write(str(self.punctuation))     # Writes the dictionary to the file.
        f.close()                    # Close the file.


    def read_model(self):
        """ reads the stored dictionaries for the called TextModel object from
        their files and assigns them to the attributes of the called TextModel.
        """

        #words dictionary
        filename = self.name + '_' + 'words'
        f = open(filename, 'r')    # Open for reading.
        d_str = f.read()           # Read in a string that represents a dict.
        f.close()
        self.words = dict(eval(d_str))      # Convert the string to a dictionary.

        #word_lengths dictionary
        filename1 = self.name + '_' + 'word_lengths'
        f = open(filename1, 'r')    # Open for reading.
        d_str1 = f.read()           # Read in a string that represents a dict.
        f.close()
        self.word_lengths = dict(eval(d_str1))      # Convert the string to a dictionary.

        #stems dictionary
        filename2 = self.name + '_' + 'stems'
        f = open(filename2, 'r')    # Open for reading.
        d_str2 = f.read()           # Read in a string that represents a dict.
        f.close()
        self.stems = dict(eval(d_str2))      # Convert the string to a dictionary.

        #sentence_lengths dictionary
        filename3 = self.name + '_' + 'sentence_lengths'
        f = open(filename3, 'r')    # Open for reading.
        d_str3 = f.read()           # Read in a string that represents a dict.
        f.close()
        self.sentence_lengths = dict(eval(d_str3))      # Convert the string to a dictionary.

        #punctuation dictionary
        filename4 = self.name + '_' + 'punctuation'
        f = open(filename4, 'r')    # Open for reading.
        d_str4 = f.read()           # Read in a string that represents a dict.
        f.close()
        self.punctuation = dict(eval(d_str4))      # Convert the string to a dictionary.

    def similarity_scores(self, other):
        """computes and returns a list of log similarity scores
        measuring the similarity of self and other
        """

        scores = [0]*5
        for i in range(len(scores)):
            if i == 0:
                words_score = compare_dictionaries(other.words, self.words)
                scores[0] = words_score
            elif i == 1:
                word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
                scores[1] = word_lengths_score
            elif i == 2:
                stems_score = compare_dictionaries(other.stems, self.stems)
                scores[2] = stems_score
            elif i == 3:
                sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
                scores[3] = sentence_lengths_score
            elif i == 4:
                punctuation_score = compare_dictionaries(other.punctuation, self.punctuation)
                scores[4] = punctuation_score

        return scores

    def classify(self, source1, source2):
        """compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2)
        and determines which of these other TextModels is the more likely source of the called TextModel.
        """

        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        s1_rounded = [ '%.3f' % elem for elem in scores1 ]
        s2_rounded = [ '%.3f' % elem for elem in scores2 ]
        print('scores for' , source1.name , s1_rounded)
        print('scores for' , source2.name , s2_rounded)

        counter1 = 0
        counter2 = 0
        for i in range(len(scores1)):
            if scores1[i] > scores2[i]:
                counter1 += 1
            else:
                counter2 += 1

        if counter1 > counter2:
            print(self.name , 'is more likely to have come from' , source1.name + "'s", "writer")
        else:
            print(self.name , 'is more likely to have come from' , source2.name+ "'s", "writer")



def compare_dictionaries(d1, d2):
    """ take two feature dictionaries d1 and d2 as inputs,
    and compute and return their log similarity score
    """

    sim_score = 0

    total_words_d1 = 0
    for i in d1:
        total_words_d1 += d1[i]

    total_words_d2 = 0
    for i in d2:
        total_words_d2 += d2[i]

    for i in d2:
        if i in d1:
            s = d1[i]/total_words_d1
            h = log(s) * d2[i]
            sim_score += h
        else:
            sim_score += log(0.5/total_words_d1) * d2[i]

    return sim_score


def run_tests():
    """ create two text bodies models and then classify three new texts and detrmine the similarity """

    #first epsiode from season 1 & 2 & 3
    source1 = TextModel('South Park')
    source1.add_file('southpark1.txt')
    source1.add_file('southpark2.txt')
    source1.add_file('southpark3.txt')

    #first epsiode from season 1 & 2 & 3
    source2 = TextModel('Family Guy')
    source2.add_file('familyguy1.txt')
    source2.add_file('familyguy2.txt')
    source2.add_file('familyguy3.txt')

    new1 = TextModel('Rick and Morty')
    new1.add_file('rickandmorty1.txt')
    new1.classify(source1, source2)
    print()
    new2 = TextModel('South Park SE 4 EP 1')
    new2.add_file('southpark4.txt')
    new2.classify(source1, source2)
    print()
    new3 = TextModel('Family Guy SE 4 EP 1')
    new3.add_file('familyguy4.txt')
    new3.classify(source1, source2)
    print()
    new4 = TextModel("Bob's Burger")
    new4.add_file('bobsburger1.txt')
    new4.classify(source1, source2)
    print()
    new5 = TextModel("Futurama")
    new5.add_file('futurama.txt')
    new5.classify(source1, source2)
    print()
    new6 = TextModel("The Simpsons")
    new6.add_file('thesimpsons1.txt')
    new6.classify(source1, source2)
