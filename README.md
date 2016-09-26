# BibCut v0.1

BibCut is a small script which uses the .aux file created in a LaTeX compliation to extract the used citekeys and build an "output.bib", which contains only the used referecnes. the full .bib file 

This little piece of software has only one intention: Using the .aux file created during LaTeX compilation,	 extracting the citekeys used, checking the full .bib file and writing the used references into a sliced .bib file which contains only the references used in the .tex file

A little caution though: The .py file must be in the same folder as the .aux file. The path to the .bib files must be dedicated	at first. Keep in mind to include all .bib files

Also it is very important to maintain a CLEAN .bib file! The template used for a standard .bib entry is the following:	
```
@article{TheCitekey,
    author = {P. Hofmann},
    title = {{Test for bibcut v0.1}},
    year = {2015},
}
```
Any other layout than that needs adjustments in parsing the .bib file. (Feel free to do so)
Also, any other layout (extra spaces, extra \t) will lead to faulty output.bib files.
So be sure to have CLEAN .bib files.

(c) 2015, PH

# BibCut v0.2

Some minor bugfixes and cosmetic stuff for export of the resulting .bib file (the output bib will now be renamed into the name of the auxilary file, i.e.: test.aux will yield in test.bib as output file).

# BibCut v0.3

Added support for python 3.x.
