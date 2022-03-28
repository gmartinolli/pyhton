import json,requests
from pprint import pprint
keyword=input('plz give me a keyword')
url1= 'https://api.datamuse.com/words?syn=' + keyword + '&max=4'
