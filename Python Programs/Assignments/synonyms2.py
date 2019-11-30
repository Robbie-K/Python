'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Oct. 24, 2014.
'''
import time

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return (sum_of_squares)**(1/2)


def cosine_similarity(vec1, vec2):
    '''Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    '''

    dotProduct = 0.0  # floating point to handle large numbers
    for key in vec1:
        if key in vec2:
            dotProduct += vec1[key] * vec2[key]

    return dotProduct / (norm(vec1) * norm(vec2))

# print(cosine_similarity({'i': 3, 'am': 3, 'a': 2, 'sick': 1, 'spiteful': 1, 'an': 1,
# 'unattractive': 1},{'i': 1, 'believe': 1, 'my': 1, 'is': 1, 'diseased': 1}))

def build_semantic_descriptors_from_files(filenames):
    combinedList = []
    for i in range(len(filenames)):
        fileList = open(filenames[i], encoding = "utf-8")
        wordList = fileList.read().lower()
        fileList.close()
        replaceStrEnd = ['!', '?']
        replaceStrPunc = [',', '-', '--', ':', ';', '"', ' s ', ' a ', "''", '\n']
        stopWordLs = [' and ', ' but ', ' the ', ' that ', ' it ',
                                ' is ', ' an ', ' in ', ' of ', ' do ',
                                ' took ', ' too ', ' to ', ' however ',
                                ' therefore ', ' not ', ' come ', ' how ',
                                ' as ', ' with ', ' i ', ' he ', ' she ',
                                ' them ', ' their ', ' if ', ' then ',
                                ' now ']
        for k in range(len(stopWordLs)):
            wordList = wordList.replace(stopWordLs[k], ' ')
            if k < len(replaceStrPunc):
                wordList = wordList.replace(replaceStrPunc[k],' ')
            if k < len(replaceStrEnd):
                wordList = wordList.replace(replaceStrEnd[k],'.')
        wordList = wordList.split('.')
        wordList = [index.split() for index in wordList]
        for j in range(len(wordList)):
            combinedList.append(wordList[j])
    dictionary = build_semantic_descriptors(combinedList)
    return dictionary


def build_semantic_descriptors(sentences):
    dictionary = {}

    for i in range(len(sentences)):
        innerDict = dictionaryBuilder(sentences[i])

        for key in innerDict:
            temp = innerDict.copy()
            del temp[key]

            if key not in dictionary:
                dictionary[key] = temp
            elif key in dictionary:
                for j in temp:
                        if j in dictionary[key]:
                            dictionary[key][j] += 1
                        else:
                            dictionary[key][j] = 1
    return dictionary

def dictionaryBuilder(sentenceList):
    innerDict = {}
    for index in sentenceList:
        if index not in innerDict:
            innerDict[index] =1
        else:
            innerDict[index] += 1
    return innerDict


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    dictionary = semantic_descriptors
    x = 0
    largest = 0
    ind = 0
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
    fileLines = open(filename, encoding = "utf-8")
    lines = fileLines.read()
    fileLines.close()
    lines = lines.split('\n')
    lines = [index.split() for index in lines]
    correct = 0
    for i in range(len(lines)):
        choice = most_similar_word(lines[i][0], lines[i][2:],
                    semantic_descriptors, cosine_similarity)
        if choice == lines[i][1]:
            correct += 1
    percentCorrect =  correct/len(lines) * 100
    return percentCorrect


def main():
    time1 = time.time()
    filenames = ['Proust.txt', 'Tolstoy.txt']
    semantic_descriptors = build_semantic_descriptors_from_files(filenames)
    time2 = time.time()
    timeTaken = time2 - time1
    print( '%.2f%% correct!\nThe test took %.2f seconds.'
            %(run_similarity_test('test.txt',semantic_descriptors,
            cosine_similarity), timeTaken))


main()
