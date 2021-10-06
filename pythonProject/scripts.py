import os
import re
from collections import Counter


def readfiles(filenamelist):
    filescontent = list()
    if filenamelist == [] or filenamelist is None:
        raise Exception('No filenames were inserted')
    for filename2 in filenamelist:
        filename = 'files/{0}'.format(filename2)
        if not os.path.isfile(filename):  # Checks if the file exists
            raise Exception("File {0} doesn't exist".format(filename2))
        if os.stat(filename).st_size == 0:  # Checks the size statistic of filename
            raise Exception('File {0} is empty'.format(filename2))
        print('Opening {0}...'.format(filename2))
        file = open(filename, 'r', encoding='utf8')
        print('Reading lines in {0}...'.format(filename2))
        lines = file.readlines()
        linescount = 0
        wordscount = 0
        wordcounter = list()
        print('Counting words and lines in {0}...'.format(filename2))
        for i in lines:
            linescount += 1  # Counts lines
            words = re.findall(r'\w+', i)  # Separates words using the \w+ filter (No !,? etc.)
            wordscount += len(words)  # Counts words
            for word in words:
                wordcounter.append(word.lower())  # Transforms all words to lowercase
        mostcommon = list(Counter(wordcounter).most_common(1))[0]
        # ^ Uses Counter to find the most common word and then transforms the very first entry to list
        print('Appending all relevant values from {0}...'.format(filename2))
        filecontent = list()
        filecontent.append(filename.split('.')[0])
        filecontent.append(filename.split('.')[1])
        filecontent.append(mostcommon[0])
        filecontent.append(mostcommon[1])
        filecontent.append(wordcounter.index(mostcommon[0]) + 1)
        filecontent.append(linescount)
        filecontent.append(wordscount)
        filecontent.append(lines)
        filescontent.append(filecontent)
        file.close()
    return filescontent


def writetext(filescontent):
    if filescontent == [] or filescontent is None:
        raise Exception('There was a mistake in processing the files')
    if os.path.isfile('output.txt'):
        answer = input('Output file already exists, continue anyway? y/n')
        if answer == 'y':
            print('Creating output.txt file...')
            file = open('output.txt', 'w', encoding='utf8')
            print('Writing into output.txt file...')
            for i in filescontent:
                file.write('\n\nFile name: {0}\n'.format(i[0]))
                file.write('File extension: .{0}\n'.format(i[1]))
                file.write('Most common word: "{0}", occurs {1} times\n'.format(i[2], i[3]))
                file.write('First found as word number: {0}\n'.format(i[4]))
                file.write('Line count: {0}\n'.format(i[5]))
                file.write('Word count: {0}\n\n'.format(i[6]))
                for i2 in i[7]:
                    file.write(i2)
        else:
            print('Operation aborted')
    else:
        print('Creating output.txt file...')
        file = open('output.txt', 'w', encoding='utf8')
        print('Writing into output.txt file...')
        for i in filescontent:
            file.write('\n\nFile name: {0}\n'.format(i[0]))
            file.write('File extension: .{0}\n'.format(i[1]))
            file.write('Most common word: "{0}", occurs {1} times\n'.format(i[2], i[3]))
            file.write('First found as word number: {0}\n'.format(i[4]))
            file.write('Line count: {0}\n'.format(i[5]))
            file.write('Word count: {0}\n\n'.format(i[6]))
            for i2 in i[7]:
                file.write(i2)
