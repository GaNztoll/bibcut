##########################################################################
##									##										##
##		BibCut v0.1						##								##
##									##									##
##########################################################################

from glob import glob
import os

# Initialising variables, read bib libraries. If you need more than 2 bib files
# you will have to create more fileobjects (fobj)

if os.name == 'nt':
	fobj = open('D:\Papers\Bib\library3.bib','r')
	fobj2 = open('D:\Promotion\References\publications.bib','r')

elif os.name == 'mac':
	fobj = open('DATA_TRANS\Papers\Bib\library3.bib','r')
	fobj2 = open('DATA_TRANS\Promotion\References\publications.bib','r')

x = []
citekey = []
words = []
parameter = []
dict = {}
dicttype = {}
citation = {}
type = 'a'

# For more .bib files, just add additional fobj to x via x.append()

for line in fobj:
	x.append(str(line))
	
for line in fobj2:
	x.append(str(line))

# And don't forget to close them here.	
	
fobj.close()	
fobj2.close()

# Parsing bib library into the following format: 
# dict{citekey: dict{word:parameter}}
# dicttype holds the information which type the .bib entry was
# (i.e. article, poster, thesis, ...)

for i in xrange(len(x)):
	if x[i][0] == '@':
		citekey = x[i].split('{')[1].split(',')[0]
		type = x[i][1:].split('{')[0]
		words = []
		parameter = []
		citation = {}
		for j in xrange(1,100):
			if x[i+j][0] == "}":
				break
			words.append(x[i+j].split('=')[0][1:-1])
			parameter.append(x[i+j].split('=')[1][1:-2])
				
		for k in xrange(len(words)):
			citation[words[k]] = parameter[k]

		dict[citekey] = citation
		dicttype[citekey] = type
		
	else:
		pass
		
# Reading auxilary File

y = glob('*.aux')[0]

fobj3 = open(y, 'r')
aux = []
aux_wo_mult = []
mult = 0

for line in fobj3:
	if line[:10] == '\citation{' :
		aux.append(line[10:-2])

fobj3.close()

for i in xrange(len(aux)):
	mult = len(aux[i].split(','))
	if mult >> 1:
		for j in xrange(mult):
			aux_wo_mult.append(aux[i].split(',')[j])
	
	else:
		aux_wo_mult.append(aux[i])
		
aux2 = list(set(aux_wo_mult))

# Writing Output.bib with only relevant references

fobj4 = open('Output.bib', 'w+')
fobj4.write('%%%%%%%%%%%%%%%%%%%%\n%% Output.bib     %%\n%%%%%%%%%%%%%%%%%%%%\n')
for i in xrange(len(aux2)):
	fobj4.write('\n@%s{%s,\n' % (dicttype[aux2[i]],aux2[i]))
	for j in xrange(len(dict[aux2[i]])):
		fobj4.write('\t%s = %s,\n' % (dict[aux2[i]].keys()[j], dict[aux2[i]].values()[j]))
	fobj4.write('}\n')

fobj4.close()
