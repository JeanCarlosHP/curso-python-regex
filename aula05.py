"""
Meta caracteres: ^ $
( )       \1
( ) ( )   \1 \2
(( )) ( ) \1 \2 \3
"""

import re
from pprint import pprint

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer coisa</p> <div>1</div>
'''

# cpf = '147.852.963-12'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([pdiv]{1,3})>(.+?)<\/\1>', texto)
# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(?:.+?)<\/(?P=tag)>', texto)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))

# for i in tags:
#     print(i)
