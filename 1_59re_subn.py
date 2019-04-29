import re

blod = re.compile(r'\*{2}(?P<blod_text>.*?)\*{2}')

text = 'Make this **blod**. This **too**.'

print('Text:',text)
print('Blod:',blod.subn(r'<b>\g<blod_text></b>',text))

