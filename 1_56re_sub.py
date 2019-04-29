import re

blod = re.compile(r'\*{2}(.*?)\*{2}')

text = 'Make this **blod**. This **too**.'

print('Text:',text)
print('Blod:',blod.sub(r'<b>\1</b>',text))
