'''Robert Karg - 10145986
Assignment 5 - semantic similarity
Credit:
Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Oct. 24, 2014.
'''
import time

# first two functions are from the starter code
def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return (sum_of_squares)**(1/2)

# i modified this one to better suit my prefered naming style
def cosine_similarity(vec1, vec2):
    '''Returns the cosine simularity of the two vectors'''

    dotProduct = 0.0  # floating point to handle large numbers
    for key in vec1:
        # this if multiplies corresponding key values and sums them
        if key in vec2:
            dotProduct += vec1[key] * vec2[key]

    return dotProduct / (norm(vec1) * norm(vec2))


def build_semantic_descriptors_from_files(filenames):
    ''' Returns the dictionary created based off the content in the files '''

    combinedList = []
    for i in range(len(filenames)):
        fileList = open(filenames[i], encoding = "utf-8")
        string = fileList.read().lower()
        fileList.close()
        # replaceWords function gets rid of punctuation and various stop words
        wordList = replaceWords(string)

        # adds every index to the combined list
        for j in range(len(wordList)):
            combinedList.append(wordList[j])
    # the function creates the dictionary with the combined list
    dictionary = build_semantic_descriptors(combinedList)
    return dictionary


def replaceWords(string):
    ''' Returns a list of words seperated by sentences '''
    # lists of things to replace
    replaceStrEnd = ['!', '?']
    replaceStrPunc = ["'", '-', '--', ':', ';', '"', ',', '\n']
    # the stop words i found either decreased time or increased accuracy
    # or both
    stopWordLs = [' and ', ' but ', ' the ', ' that ', ' it ',
                    ' is ', ' an ', ' in ', ' of ', ' do ', ' now ',
                    ' took ', ' too ', ' to ', ' however ', ' nor ',
                    ' therefore ', ' not ', ' come ', ' how ', ' yet ',
                    ' as ', ' with ', ' he ', ' she ', ' or ', ' us ',
                    ' them ', ' their ', ' if ', ' then ', ' myself ',
                    ' than ', ' so ', ' you ', ' they ', ' his ', ' hers ',
                    ' just ', ' know ', ' also ', ' again ', ' a ', ' s ']

    # this loops through all the lists and replaces each entry in them
    for k in range(len(stopWordLs)):
        string = string.replace(stopWordLs[k], ' ')
        if k < len(replaceStrPunc):
            string = string.replace(replaceStrPunc[k],' ')
        if k < len(replaceStrEnd):
            string = string.replace(replaceStrEnd[k],'.')
    # making the string a list and getting rid of spaces
    wordList = string.split('.')
    wordList = [index.split() for index in wordList]
    return wordList


def build_semantic_descriptors(sentences):
    ''' Returns the dictionary for every sentence '''
    dictionary = {}

    # loops through and adds values or keys for every word in every sentence
    for i in range(len(sentences)):
        # a function that builds dicitonaries for every sentence
        innerDict = dictionaryBuilder(sentences[i])

        # creates the dictionaries for every word and adds to the inner
        # dictionaries if they already exist or creates a new key in the inner
        # dictionary if it does not
        for key in innerDict:
            temp = innerDict.copy()
            del temp[key]

            if key not in dictionary:
                dictionary[key] = temp
            else:
                for j in temp:
                        if j in dictionary[key]:
                            dictionary[key][j] += 1
                        else:
                            dictionary[key][j] = 1
    return dictionary


def dictionaryBuilder(sentenceList):
    ''' Returns a dictionary of the sentence '''

    innerDict = {}
    # adds the index's as keys to the dictionary
    for index in sentenceList:
        if index not in innerDict:
            innerDict[index] =1
        # in case a word occurs twice in a given sentence
        else:
            innerDict[index] += 1
    return innerDict


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    ''' Returns the word the function determines is most similar'''

    # using the semantic_descriptors (in my main function) as the dictionary
    dictionary = semantic_descriptors
    x = 0
    largest = 0
    ind = 0
    # this loop keeps track of the largest value and returns the choice that
    # corresponds to it
    for i in range(len(choices)):
        temp = x
        try:
            x = similarity_fn(dictionary[word], dictionary[choices[i]])
        except KeyError:
            x = -1

        if x > temp:
            temp = x
            ind = i
    return choices[ind]


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    ''' Tests what percentage the AI got correct and returns it '''

    fileLines = open(filename, encoding = "utf-8")
    lines = fileLines.read()
    fileLines.close()
    lines = lines.split('\n')
    lines = [index.split() for index in lines]
    correct = 0
    # getting the AIs choice for every "question" (line) of the file
    for i in range(len(lines)):
        choice = most_similar_word(lines[i][0], lines[i][2:],
                    semantic_descriptors, cosine_similarity)
        # adds 1 if correct
        if choice == lines[i][1]:
            correct += 1
    # this gives the percentage
    percentCorrect =  correct/len(lines) * 100
    return percentCorrect

# i left this to make it easier for you to run
tic = time.clock()
dict = build_semantic_descriptors_from_files(('Proust.txt', 'Tolstoy.txt'))
toc = time.clock()
print('Time elapsed: ', toc - tic)
res = run_similarity_test('test.txt', dict, cosine_similarity)
print(res)
