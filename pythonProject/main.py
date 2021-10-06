from scripts import readfiles, writetext


filenamelist = ['Bible.txt', 'Godlike Comedy.txt', 'Way of the Leader.txt']
filescontent = readfiles(filenamelist)
writetext(filescontent)
print('Process finished, open output.txt for results.')
