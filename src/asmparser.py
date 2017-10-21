#Parser file which defines grammer and parsing


from pyparsing import Word, alphas
greet = Word( alphas ) + Word ( alphas )  # <-- grammar defined here
asmfileptr = open("../data/asm.txt",'r')

asmfile = asmfileptr.read()

#print(asmfile)

print (asmfile, "->", greet.parseString( asmfile ))

