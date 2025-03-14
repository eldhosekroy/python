from nltk import CFG, ChartParser
grammer=CFG.fromstring("""
S -> NP VP
NP -> DT NN
VP -> VBZ NP
DT -> 'the'
NN -> 'cat'|'dog'
VBZ -> 'chases'
""")
parser=ChartParser(grammer)
sentence="the cat chases the dog".split()
for tree in parser.parse(sentence):
	print(tree)

