#Parser file which defines grammer and parsing


from pyparsing import *

file = open( "../data/asm.txt", "r" )

fl = file.readlines()

curlen = 0
for curlen in range(len(fl)):
    fl[curlen] = fl[curlen].strip('\n')

print(fl)

file.close()
