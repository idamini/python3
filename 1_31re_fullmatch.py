import re

text = 'This is some text -- with punctuation.'
pattern = 'is'

print('Text   :',text)
print('pattern:',pattern)

m = re.search(pattern,text)
print('Search  :',m)
s = re.fullmatch(pattern,text)
print('Full match  :',s)
