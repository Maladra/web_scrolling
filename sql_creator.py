import json
import sqlite3

class Citation:
    def __init__(self,text,author,tags):
        self.text = text
        self.author = author
        self.tags = tags
        self.counter_author = 1

class Tag:
    def __init__(self,tag):
        self.tag = tag
        self.counter_tag = 1

## supportest@support.viacesi.info
####################
## STAT by Author ##
####################
#citation_array = []
#add = True
#with open('citation/citation.json') as json_file:
#    data = json.load(json_file)
#    for p in data:
#        for item in citation_array:
#            if item.author == p['author']:
#                item.counter_author = item.counter_author+1
#                add = False
#                break
#        if add :
#                citation = Citation(p['text'],p['author'],p['tags'])
#                citation_array.append(citation)
#        add = True


#################
## STAT by Tag ##
#################
#tag_array = []
#i = 0
#add = True
#with open('citation/citation.json') as json_file:
#    data = json.load(json_file)
#    for p in data:
#        for tag in p['tags']:
#            for item in tag_array:
#                if tag == item.tag:
#                    item.counter = item.counter+1
#                    add = False
#                    break
#            if add : 
#                tag = Tag(p['tags'])
#                tag_array.append(tag)
#            add = True
#            print (i)
#            i = i+1
#
#
#print (len(tag_array))


conn = sqlite3.connect('citation.db')
c = conn.cursor()

