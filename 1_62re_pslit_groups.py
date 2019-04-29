import re

text ='''Paragraph one
on two lines.
paragraph two.


paragraph three.'''

print('with split:')
for num,para in enumerate(re.split(r'\n{2,}',text)):
    print(num,repr(para))
    print()
