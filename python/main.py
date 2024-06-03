import json, os, glob 
from operator import itemgetter

entries = []

for filename in glob.glob(os.path.join('data/', '*.json')):
    with open(filename, encoding='utf-8', mode='r') as currentFile:
      data = json.loads(currentFile.read())
      for i in data['entries']:
        entries.append(i)

with open('./python/data/data.json', 'w') as file:
    json.dump(sorted(entries, key=itemgetter('published')), file, indent= 4, ensure_ascii=True)
