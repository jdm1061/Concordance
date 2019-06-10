# -*- coding: utf-8 -*-
"""
@author: MARTIJ

This script takes any text copied to the clipboard and creates a concordance.
saves results to a text file 
will later take the created dictionary and pass it to a csv file
"""
import re
import pprint
import pyperclip


text = pyperclip.paste() ##enters text on clipboard into the program
text = text.lower() ## makes all letters lowercase. didn't want to have capitalized words seperated

textRegex = re.compile(r'\w+') ## creates list of words from the text
mo = textRegex.findall(text) ##creates a list of words in the text, mo for matched objects

textDic = {} ##dictionary to track word counts

##below: takes each word in the list, checks if it is already in the dictionary
## if word is not in the dictionary it is added
##if it is in the dictionary it adds 1 to the word count
for i in range(len(mo)):
    if mo[i] not in textDic.keys():
        textDic[mo[i]]=1
    else:
        textDic[mo[i]] += 1

#pprint.pprint(textDic) ##prints out the words and word counts in easy to read format once the dictionary is complete
#print('Total word count: %s' %len(mo))
        
        
### Takes the result of the search and saves it to a text file
### file includes total word count and number of unique words
### Informs user of the current location of the text file in the shell     
fileName = r'C:\temp\test_folder\concordance_results.txt'
saveFile = open(fileName,'w')
saveFile.write('Total word count: %s \n' %len(mo))
saveFile.write('Total Unique words: %s \n' %str(len(textDic.keys())))
saveFile.write('Number of times each word appears: \n')
saveFile.write(str(pprint.pformat(textDic)))
saveFile.close()
print('Results saved in the folllowing folder and file:\n'+ fileName)



