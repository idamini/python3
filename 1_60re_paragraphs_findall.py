import re

text ='''Paragraph one
on two lines.

paragraph two.


paragraph three.'''

for num,para in enumerate(re.findall(r'(.+?)\n{2,}',text,flags = re.DOTALL)):
    print(num,repr(para))
    print()
