import json

with open('citation/citation.json') as json_file:
    data = json.load(json_file)
    for p in data:
        print(p['text'])
        for author in p['author']:
            if author != '- ':
                print(author)


