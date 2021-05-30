"""
Meta caracteres: ^ $ ( )
* 0 ou n
+ 1 ou n {1,}
? 0 ou 1
"""

import re

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer coisa</p> <div></div>
'''

print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))
