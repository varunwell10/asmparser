#Parser file which defines grammer and parsing


from pyparsing import *

file = open( "../data/qsort.txt", "r" )

fl = file.read()

curlen = 0
#for curlen in range(len(fl)):
    #fl[curlen] = fl[curlen].strip('\n')

print("number of 'movl' instructions: " , fl.count("movl"))

file.close()
