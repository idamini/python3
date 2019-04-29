import re

text ='''Paragraph one
on two lines.

paragraph two.


paragraph three.'''
print('with finadll:')
for num,para in enumerate(re.findall(r'(.+?)(\n{2,}|$)',
                                     text,
                                     flags = re.DOTALL)):
    print(num,repr(para))
    print()

print()
print('with split:')
for num,para in enumerate(re.split(r'\n{2,}',text)):
    print(num,repr(para))
    print()
