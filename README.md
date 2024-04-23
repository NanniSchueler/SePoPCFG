# SePoPCFG
## About
Copy Abstract here!

## Installation + Requirements
This tool is based on the PCFG Cracker by Weir et al. [Link to GitHub](https://github.com/lakiw/pcfg_cracker)

Before downloading our tool you need Python3 installed on your machine.
All requirements are listed in the requirements.txt file.

Note: Windows users might have problems installing fasttext, as this is only tailored to Linux and Unix systems (according to their [webseite](https://fasttext.cc/docs/en/support.html)
Use [this link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#fasttext) or [this link](https://pypi.tuna.tsinghua.edu.cn/simple/gensim/) to find and download the correct wheel file for you system and restart your programm.
We included our used version in this git, you can locally install it by using pip.

## Quick Start Guide
After downloading and installing all requirements, simply execute the 'execute.py' file.

##TODO: Finish QSG (Copied from execute.py:)
This file executes all steps of PCFG automatically.
We used our best parameters, that are
* word-embedding: Glove Twitter 200
* l = 8 (TBC)
* k = 425 (number of nearest neighbors in the embedding)
* n = 3 (TBC)

To define a password policy, enter
* (1) minimum required length (example: 4)
* (2) minimum amount of digits (example: 2)
* (3) mimimum amount of special characters (example: 1)

This results in parameter **(-p)4#2#1**

If no policy is required either set all to 0 or delete the parameter
